# -*- coding: utf-8 -*-
from odoo import api, fields, models

class BOMLine(models.Model):

    _inherit = 'mrp.bom.line'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")


class MRPProduction(models.Model):

    _inherit = 'mrp.production'

    product_image = fields.Binary(string="Image", related="product_id.image_medium")
