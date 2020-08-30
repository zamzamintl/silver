# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    employee_number = fields.Char('Employee Number', default="Auto",  copy=False, help="Employee Number")

    _sql_constraints = [
        ('employee_number', 'unique (employee_number)', 'Employee Number already exist and must be unique !')
    ]

    @api.model
    def create(self, vals):
        if vals.get('employee_number', 'Auto') == 'Auto':
            vals['employee_number'] = self.env['ir.sequence'].next_by_code('employment_number') or 'No Sequence'
        result = super(HrEmployee, self).create(vals)
        return result
