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

from datetime import datetime, timedelta

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import logging

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools import pycompat
from odoo.tools import float_is_zero, float_compare



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
