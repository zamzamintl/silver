# Copyright 2018 Giacomo Grasso <giacomo.grasso.82@gmail.com>
# Odoo Proprietary License v1.0 see LICENSE file

import datetime
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class SaleOrder(models.Model):
    _inherit = "sale.order"

    treasury_date = fields.Date(string="Treasury Date")
    forecast_id = fields.Many2one(
        comodel_name='treasury.forecast', compute="_compute_treasury_forecast",
        store=True)
    amount_main_currency = fields.Monetary(
        string='Amount Currency', compute='_compute_amount_main_currency',
        store=True)

    @api.depends('amount_to_invoice', 'pricelist_id', 'validity_date')
    def _compute_amount_main_currency(self):
        for order in self:
            if not order.validity_date:
                continue
            main_currency = order.company_id.currency_id
            order_currency = order.currency_id
            order.amount_main_currency = order_currency._convert(
                order.amount_to_invoice, main_currency, order.company_id,
                order.validity_date)

    @api.depends('treasury_date', 'state')
    def _compute_treasury_forecast(self):
        """Link sale order to a forecast template when setting
        the treasury date"""

        for item in self:
            if item.state == "cancel" or not item.treasury_date:
                item.forecast_id = False
            else:
                forecast_obj = self.env['treasury.forecast']
                forecast_id = forecast_obj.search([
                    ('date_start', '<=', item.treasury_date),
                    ('date_end', '>=', item.treasury_date),
                    ('state', '=', 'open')])
                if forecast_id:
                    item.forecast_id = forecast_id[0].id

    @api.onchange('validity_date')
    def onchange_validity_date(self):
        if self.validity_date:
            self.treasury_date = self.validity_date


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    treasury_date = fields.Date(string="Treasury Date")
    forecast_id = fields.Many2one(
        comodel_name='treasury.forecast', compute="_compute_treasury_forecast",
        store=True)
    amount_main_currency = fields.Monetary(
        string='Amount Currency', compute='_compute_amount_main_currency',
        store=True)

    @api.depends('amount_to_invoice', 'currency_id', 'date_order')
    def _compute_amount_main_currency(self):
        for order in self:
            if not order.date_order:
                continue
            main_currency = order.company_id.currency_id
            order_currency = order.currency_id
            order.amount_main_currency = order_currency._convert(
                order.amount_to_invoice, main_currency, order.company_id,
                order.date_order)

    @api.depends('treasury_date', 'state', '')
    def _compute_treasury_forecast(self):
        """Link purchase order to a forecast template
        when setting the treasury date"""
        for item in self:
            if item.state == "cancel" or not item.treasury_date:
                item.forecast_id = False
            else:
                forecast_obj = self.env['treasury.forecast']
                forecast_id = forecast_obj.search([
                    ('date_start', '<=', item.treasury_date),
                    ('date_end', '>=', item.treasury_date),
                    ('state', '=', 'open')])
                if forecast_id:
                    item.forecast_id = forecast_id[0].id

    @api.onchange('date_order')
    def onchange_date_order(self):
        if self.date_order:
            self.treasury_date = self.date_order.date()
