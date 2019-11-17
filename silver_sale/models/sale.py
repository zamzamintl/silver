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


from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one('hr.employee', 'Sales Rep')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        if self.partner_id and self.partner_id.sale_order_template_id:
            self.sale_order_template_id = self.partner_id.sale_order_template_id


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand_id = fields.Many2one(
        'product.brand', related='product_id.product_brand_id',
        string='Brand', readonly=True
    )

    available_qty = fields.Float(string='Available Qty',
                                 compute="_compute_available_qty",
                                 readonly=True)

    @api.multi
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
