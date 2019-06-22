# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta


class ExpenseTemplate(models.Model):
    _name = 'hr.expense.template'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "start_date desc, id desc"

    _description = 'Expense Template Line'

    @api.model
    def _default_employee_id(self):
        return self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)

    @api.model
    def _default_product_uom_id(self):
        return self.env['uom.uom'].search([], limit=1, order='id')

    @api.model
    def _get_employee_id_domain(self):

        res = [('id', '=', 0)]  # Nothing accepted by domain, by default
        if self.user_has_groups('hr_expense.group_hr_expense_manager') or self.user_has_groups(
                'account.group_account_user'):
            res = []  # Then, domain accepts everything
        elif self.user_has_groups('hr_expense.group_hr_expense_user') and self.env.user.employee_ids:
            employee = self.env.user.employee_ids[0]
            res = ['|', '|', ('department_id.manager_id.id', '=', employee.id),
                   ('parent_id.id', '=', employee.id), ('expense_manager_id.id', '=', employee.id)]
        elif self.env.user.employee_ids:
            employee = self.env.user.employee_ids[0]
            res = [('id', '=', employee.id)]
        return res

    name = fields.Char('Description', required=True)
    start_date = fields.Date(default=fields.Date.context_today, string="Start Date", required=1)
    last_expense_date = fields.Date(string="Start Date")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, default=_default_employee_id,
                                  domain=lambda self: self._get_employee_id_domain())
    product_id = fields.Many2one('product.product', string='Product', domain=[('can_be_expensed', '=', True)],
                                 required=True)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', required=True,
                                     default=_default_product_uom_id)
    unit_amount = fields.Float("Unit Price", required=True, digits=dp.get_precision('Product Price'))
    quantity = fields.Float(required=True, digits=dp.get_precision('Product Unit of Measure'), default=1)
    tax_ids = fields.Many2many('account.tax')
    untaxed_amount = fields.Float("Subtotal", store=True, compute='_compute_amount', digits=dp.get_precision('Account'))
    total_amount = fields.Monetary("Total", compute='_compute_amount', store=True, currency_field='currency_id',
                                   digits=dp.get_precision('Account'))

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id)
    description = fields.Text('Notes...')
    payment_mode = fields.Selection([
        ("own_account", "Employee (to reimburse)"),
        ("company_account", "Company")
    ], default='own_account', string="Paid By")
    active = fields.Boolean(string="", )
    expense_ids = fields.One2many(comodel_name="hr.expense", inverse_name="template_id", string="Expenses",
                                  required=False, )

    occurrence_period = fields.Integer(string="Occurrence Period", required=True, default=1)
    occurrence_type = fields.Selection(string="", selection=[('weekly', 'Weekly'), ('monthly', 'Monthly'),
                                                             ('annual', 'Annual')], required=False, default='monthly')

    @api.depends('quantity', 'unit_amount', 'tax_ids', 'currency_id')
    def _compute_amount(self):
        for expense in self:
            expense.untaxed_amount = expense.unit_amount * expense.quantity
            taxes = expense.tax_ids.compute_all(expense.unit_amount, expense.currency_id, expense.quantity,
                                                expense.product_id, expense.employee_id.user_id.partner_id)
            expense.total_amount = taxes.get('total_included')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            if not self.name:
                self.name = self.product_id.display_name or ''
            self.unit_amount = self.product_id.price_compute('standard_price')[self.product_id.id]
            self.product_uom_id = self.product_id.uom_id
            self.tax_ids = self.product_id.supplier_taxes_id
            account = self.product_id.product_tmpl_id._get_product_accounts()['expense']
            if account:
                self.account_id = account

    def generate_expenses(self):
        templates = self.env['hr.expense.template'].search([])
        for template in templates:
            old_date = None
            if template.last_expense_date:
                old_date = template.last_expense_date
            elif template.start_date:
                old_date = template.start_date
            else:
                raise exceptions.ValidationError('You Must Fill Start Date !')
            next_date = self.get_next_date(old_date)

    def get_next_date(self, old_date, tmpl):
        if tmpl.occurrence_type == 'weekly':
            return old_date + timedelta(days=(tmpl.occurrence.period * 7))
        elif tmpl.occurrence_type == 'monthly':
            return old_date + relativedelta(months=tmpl.occurrence.period)
        elif tmpl.occurrence_type == 'annual':
            return old_date + relativedelta(months=(tmpl.occurrence.period * 12))


class HrExpense(models.Model):
    _inherit = "hr.expense"

    template_id = fields.Many2one(comodel_name="hr.expense.template", string="Expense Template", required=False, )
