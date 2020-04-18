# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def get_activity_context(self):
        emp_id = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
        return {
            'default_res_model_id': self.env.ref("hr.model_hr_employee").id,
            'default_res_id': emp_id.id,
        }
