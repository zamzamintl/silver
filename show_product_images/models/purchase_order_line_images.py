# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Purchase(models.Model):

    _inherit = 'purchase.order.line'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")
