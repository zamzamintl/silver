from odoo import models, fields, api


class hdl_add_image_purchase(models.Model):
    _inherit = 'purchase.order'







class hdl_add_image__lines_purchase(models.Model):
    _inherit = 'purchase.order.line'

    image = fields.Binary(related="product_id.image_1920",string='Image')
