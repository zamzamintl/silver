from odoo import models, fields, api


class category(models.Model):
    _inherit = 'product.category'
    visible = fields.Boolean("visible",default = True )
