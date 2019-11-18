# -*- coding: utf-8 -*-



from odoo import fields, models


class DiscountPurchaseReport(models.Model):
    _inherit = 'purchase.report'

    discount = fields.Float('Discount', readonly=True)

    def _select(self):
        res = super(DiscountPurchaseReport,self)._select()
        select_str = res+""",sum(l.product_uom_qty / u.factor * u2.factor * cr.rate * l.price_unit * l.discount / 100.0)
         as discount"""
        return select_str
