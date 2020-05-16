# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class IrRule(models.Model):
    _inherit = 'ir.rule'

    @api.model
    def _eval_context(self):
        res = super(IrRule, self)._eval_context()
        if self.env.user.has_group('base.group_user'):
            current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
            users = []
            if current_employee:
                child_ids = self.env['hr.employee'].search([('parent_id', 'child_of', current_employee.id)])
                if child_ids:
                    user_ids = child_ids.mapped('user_id')
                    if user_ids:
                        users = user_ids.ids
            print(users)
            res.update({'users': users})
        return res
