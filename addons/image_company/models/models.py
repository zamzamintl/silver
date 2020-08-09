from odoo import api, fields, models
class company(models.Model):
    _inherit = 'res.company'
    logo_profile = fields.Binary('Slogan')
    photo = fields.Binary('Photo')
