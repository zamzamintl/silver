
from odoo import models, fields, api


class hdl_add_image_inventory(models.Model):
    _inherit = 'stock.picking'

    image = fields.Binary(string='Image')
