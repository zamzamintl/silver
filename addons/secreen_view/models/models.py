
from odoo import models, fields, api


class secreen_view(models.Model):
    _inherit ='mrp.workcenter'
    preparation = fields.Boolean("Preparation")
    washing = fields.Boolean("Washing")
    covering = fields.Boolean("Covering")
    other_workcenter = fields.Boolean("Other")
class warehouse(models.Model):
    _inherit ='stock.location'
    purchase_order = fields.Boolean("Purchase Order")
    pisonaj = fields.Boolean("pisonaj INV")
    washing_inv = fields.Boolean("Washing Inv")
