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

from datetime import datetime, timedelta

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import logging

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools import pycompat

_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit= "crm.lead"

    code=fields.Char(string="Code",default='/',readonly=True)


    @api.model
    def create(self, values):
        if (not values.get('code', False) or values['code'] == _('/')) :
            new_code = self.env['ir.sequence'].next_by_code('crm.lead')
            values['code'] = new_code
        lead = super(Lead, self).create(values)
        return lead


