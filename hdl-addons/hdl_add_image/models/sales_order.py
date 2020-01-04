# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hdl_add_image(models.Model):
    _inherit = 'sale.order'

    image = fields.Binary(string='Image')

