from odoo import models, fields, api


class hdl_add_image_purchase(models.Model):
    _inherit = 'purchase.order'

    image = fields.Binary(string='Image')
