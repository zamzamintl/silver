# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockPicking(models.Model):

    _inherit = 'stock.move'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")


class StockMoveLine(models.Model):

    _inherit = 'stock.move.line'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")
