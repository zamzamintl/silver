# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hdl_add_image(models.Model):
    _inherit = 'sale.order'




class hdl_add_line_image(models.Model):
    _inherit = 'sale.order.line'

    image = fields.Binary(related="product_id.image_1920",string='Image')

