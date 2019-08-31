# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    member_type = fields.Selection(string="Member Type",
                                   selection=[('duration', 'By Duration')],
                                   required=False,
                                   default='duration')

    duration = fields.Selection(string="Member Duration",
                                selection=[('monthly', 'Monthly'), ('quarterly', 'Quarterly'),
                                           ('half_year', 'Half Year'), ('yearly', 'Yearly')],
                                required=False,
                                default='monthly')

