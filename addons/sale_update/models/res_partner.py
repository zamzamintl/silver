# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2018-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################



from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError, ValidationError



class ResPartner(models.Model):
    _inherit = 'res.partner'
    sale_order_template_id = fields.Many2one(
        'sale.order.template', 'Quotation Template')


