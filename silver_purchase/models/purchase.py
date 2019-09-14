# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2019-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    partner_ids=fields.Many2many(comodel_name='res.partner',
                                 relation='partner_purchase_rel'
                                 ,column1="partner_col",
                                 column2='purchase_order_col',
                                 string='Customers',
                                 domain=[('customer','=',True)])


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_brand_id = fields.Many2one(
        'product.brand',related='product_id.product_brand_id',
        string='Brand',readonly=True
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

    @api.depends('product_id')
    def _compute_available_qty(self):
        for ln in self:
            if ln.product_id:
                available_qty = ln.product_id.with_context(company_owned=True).qty_available
                ln.available_qty = available_qty


