# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
import odoo.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
import pytz


class HrExpense(models.Model):
    _inherit = "hr.expense"

    template_id = fields.Many2one(comodel_name="hr.expense.template",
                                  string="Expense Template", required=False, )
