from odoo import models, fields, api


class category(models.Model):
    _inherit = 'product.category'
    hidden = fields.Boolean("Hidden",default = False )
