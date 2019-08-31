# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    template_ids = fields.Many2many(comodel_name="sale.order.template", string="Multi Quotation Templates", )

    @api.onchange('template_ids')
    def onchange_template_ids(self):
        if self.template_ids:
            lines = []
            option_lines = []
            self.order_line = False
            for template in self.template_ids:
                for line in template.sale_order_template_line_ids:
                    data = self._compute_line_data_for_template_change(line)
                    if line.product_id:
                        discount = 0
                        if self.pricelist_id:
                            price = self.pricelist_id.with_context(uom=line.product_uom_id.id).get_product_price(
                                line.product_id, 1, False)
                            if self.pricelist_id.discount_policy == 'without_discount' and line.price_unit:
                                discount = (line.price_unit - price) / line.price_unit * 100
                                price = line.price_unit

                        else:
                            price = line.price_unit

                        data.update({
                            'price_unit': price,
                            'discount': 100 - ((100 - discount) * (100 - line.discount) / 100),
                            'product_uom_qty': line.product_uom_qty,
                            'product_id': line.product_id.id,
                            'product_uom': line.product_uom_id.id,
                            'customer_lead': self._get_customer_lead(line.product_id.product_tmpl_id),
                        })
                        if self.pricelist_id:
                            data.update(
                                self.env['sale.order.line']._get_purchase_price(self.pricelist_id, line.product_id,
                                                                                line.product_uom_id,
                                                                                fields.Date.context_today(self)))
                    lines.append((0, 0, data))

                for option in template.sale_order_template_option_ids:
                    data = self._compute_option_data_for_template_change(option)
                    option_lines.append((0, 0, data))

                if template.number_of_days > 0:
                    self.validity_date = fields.Date.to_string(datetime.now() + timedelta(template.number_of_days))

                self.require_signature = template.require_signature
                self.require_payment = template.require_payment

                if template.note:
                    self.note = template.note

            self.order_line = lines
            self.order_line._compute_tax_id()
            self.sale_order_option_ids = option_lines
