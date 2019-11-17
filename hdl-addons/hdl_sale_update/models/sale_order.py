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


from odoo import models, fields, api, _
from datetime import date, datetime, time, timedelta
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('crm.lead.tag', 'sale_crm_tag_rel', 'lead_id', 'tag_id', string='Tags', help="Classify and analyze your lead/opportunity categories like: Training, Service")


