# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):

    _inherit = 'sale.order.line'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")
