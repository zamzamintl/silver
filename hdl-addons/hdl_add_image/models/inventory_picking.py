
from odoo import models, fields, api


class hdl_add_image_inventory(models.Model):
    _inherit = 'stock.picking'


class hdl_add_image_lines_inventory(models.Model):
    _inherit = 'stock.move'

    image = fields.Binary(related="product_id.image_1920",string='Image')

