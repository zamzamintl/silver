# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Invoice(models.Model):

    _inherit = 'account.invoice.line'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")
