# Copyright 2018 Giacomo Grasso <giacomo.grasso.82@gmail.com>
# Odoo Proprietary License v1.0 see LICENSE file

from odoo import models, fields, api, _
from odoo.tools.misc import formatLang
from datetime import timedelta
from odoo.exceptions import UserError


class TreasuryForecast(models.Model):
    _inherit = "treasury.forecast"

    sale_order_ids = fields.One2many(comodel_name='sale.order', inverse_name='forecast_id',
                                     string='Sale orders')
    purchase_order_ids = fields.One2many(comodel_name='purchase.order', inverse_name='forecast_id',
                                         string='Sale orders')

    # fields for treasury analysis
    sales = fields.Float('Sales', compute='_compute_sales', store=True)
    open_sales = fields.Float('Open sales', compute='_compute_sales', store=True)
    purchases = fields.Float('Purchases', compute='_compute_purchases', store=True)
    open_purchases = fields.Float('Open purchases', compute='_compute_purchases', store=True)

    @api.depends('sale_order_ids', 'sale_order_ids.amount_total',
                 'sale_order_ids.amount_main_currency')
    def _compute_sales(self):
        for item in self:
            total, due = 0.0, 0.0
            for order in item.sale_order_ids:
                total += order.amount_total
                due += order.amount_main_currency
            item.sales, item.open_sales = total, due

    @api.depends('purchase_order_ids', 'purchase_order_ids.amount_total',
                 'purchase_order_ids.amount_main_currency')
    def _compute_purchases(self):
        for item in self:
            total, due = 0.0, 0.0
            for line in item.purchase_order_ids:
                total += line.amount_total
                due += line.amount_main_currency
            item.purchases, item.open_purchases = total, due

    @api.depends('payables', 'open_payables', 'receivables', 'open_receivables',
                 'other_flows', 'open_flows', 'sales', 'open_sales',
                 'purchases', 'open_purchases')
    def _compute_periodic_saldo(self):
        for item in self:

            item.periodic_saldo = sum([item.open_receivables, item.open_payables, item.other_flows,
                                      item.open_sales, -item.open_purchases])

            # creating the forecast analysis table
            header = (_(""), _("Receivables"), _("Payables"), _("Sales"), _("Purchases"), _("Other"))
            report_lines = (
                (_("Total"), item.receivables, item.payables, item.sales, -item.purchases, item.other_flows),
                (_("Open"), item.open_receivables, item.open_payables, item.open_sales, -item.open_purchases, item.open_flows)
                )

            item.forecast_analysis = self._tuple_to_table(
                'forecast', '', header, None, report_lines)

    def compute_forecast_data(self):
        for rec in self:
            super(TreasuryForecast, rec).compute_forecast_data()

            # adding sale orders
            so_obj = self.env['sale.order']
            so_list = so_obj.search([
                ('treasury_date', '>=', rec.date_start),
                ('treasury_date', '<=', rec.date_end),
                ('forecast_id', '=', False),
            ])

            for so in so_list:
                so.update({'forecast_id': rec.id})

            # adding purchase orders
            po_obj = self.env['purchase.order']
            po_list = po_obj.search([
                ('treasury_date', '>=', rec.date_start),
                ('treasury_date', '<=', rec.date_end),
                ('forecast_id', '=', False),
            ])

            for po in po_list:
                po.update({'forecast_id': rec.id})

    @api.multi
    def sett_mass_date(self):
        """Adding PO and SO to the method."""
        self.ensure_one()
        super(TreasuryForecast, self).sett_mass_date()

        sale_orders = self.sale_order_ids.filtered(lambda r: r.amount_main_currency != 0.0)
        sale_orders.update({'treasury_date': self.set_mass_date})
        purchase_orders = self.purchase_order_ids.filtered(lambda r: r.amount_main_currency != 0.0)
        purchase_orders.update({'treasury_date': self.set_mass_date})
