# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class /opt/odoo/custom/scaffold(models.Model):
#     _name = '/opt/odoo/custom/scaffold./opt/odoo/custom/scaffold'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    reference_doc_id = fields.Reference(
        [
        ('stock.picking','Delivery'),
        ('event.event','Event'),
        ('product.product','Product'),
        ('project.project','Project'),
        ('sale.order','Order'),
        ('repair.order','Repair'),
        ('sale.subscription','Subscription'),
        ],
        string='In Reference to')


