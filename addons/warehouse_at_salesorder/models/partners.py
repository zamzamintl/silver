
from odoo import api, fields ,models

class partner(models.Model):
    _inherit = 'res.partner'
    default_purchase_oer = fields.Boolean(default=False,string="Default vendor")