# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2018-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################


from odoo import models, fields, api, _
from datetime import date, datetime, time, timedelta
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    template_ids = fields.Many2many(comodel_name="sale.order.template", string="Multi Quotation Templates", )
    tag_ids = fields.Many2many('crm.lead.tag', 'sale_crm_tag_rel', 'lead_id', 'tag_id', string='Tags', help="Classify and analyze your lead/opportunity categories like: Training, Service")
    employee_id = fields.Many2one('hr.employee', 'Sales Rep')


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
        else:
            self.order_line=False

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        if self.partner_id and self.partner_id.sale_order_template_id:
            self.sale_order_template_id = self.partner_id.sale_order_template_id

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'



    available_qty = fields.Float(string='Available Qty',
                                 compute="_compute_available_qty",
                                 readonly=True)

    @api.onchange('product_id')
    def product_id_change_check_duplicated(self):
        self.ensure_one()
        if self.product_id and self.order_id:
            order_lines = self.order_id.order_line.filtered(
                lambda l: l.product_id.id == self.product_id.id)
            if len(order_lines) > 2:
                raise ValidationError(
                    _('You Have already added this product before'))

    @api.depends('product_id', 'order_id.warehouse_id')
    def _compute_available_qty(self):
        for ln in self:
            if ln.product_id and ln.order_id.warehouse_id:
                available_qty = ln.product_id.with_context(
                    warehouse=ln.order_id.warehouse_id.id).qty_available

                ln.available_qty = available_qty
