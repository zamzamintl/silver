# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
import odoo.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
import pytz


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
    last_expense_date = fields.Date(string="Last Expense Date")
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
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account',
                                          oldname='analytic_account')
    analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Analytic Tags', )

    active = fields.Boolean(string="", default=True)
    expense_ids = fields.One2many(comodel_name="hr.expense", inverse_name="template_id", string="Expenses",
                                  required=False, )
    expense_count = fields.Integer(string="Expenses", required=False, compute="get_expense_count")
    occurrence_period = fields.Integer(string="Occurrence Period", required=True, default=1)
    occurrence_type = fields.Selection(string="", selection=[('weekly', 'Weekly'), ('monthly', 'Monthly'),
                                                             ('annual', 'Annual')], required=False, default='monthly')

    def action_open_expenses(self):
        return {
            'name': _('Expenses'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form,search',
            'res_model': 'hr.expense',
            'target': 'current',
            'domain': [('template_id', '=', self.id)],
            'context': {'default_template_id': self.id},

        }

    def get_expense_count(self):
        self.expense_count = len(self.expense_ids.ids)

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
            next_date = None
            if template.last_expense_date:
                old_date = template.last_expense_date
            elif template.start_date:
                next_date = template.start_date
            else:
                raise exceptions.ValidationError('You Must Fill Start Date !')
            if not next_date:
                next_date = self.get_next_date(old_date, template)
            tz = pytz.timezone(template.employee_id.tz)
            if not tz:
                tz=pytz.UTC
            current_date = datetime.now(tz=tz).date()
            if next_date <= current_date:
                vals = {
                    'name': template.name,
                    'product_id': template.product_id.id,
                    'analytic_account_id': template.analytic_account_id.id,
                    'analytic_tag_ids': template.analytic_tag_ids.ids,
                    'tax_ids': template.tax_ids.ids,
                    'unit_amount': template.unit_amount,
                    'quantity': template.quantity,
                    'employee_id': template.employee_id.id,
                    'date': Date.to_string(next_date),
                    'template_id': template.id,
                }
                res = self.env['hr.expense'].create(vals)
                template.write({'last_expense_date': Date.to_string(next_date)})
                mail_template = self.env.ref('danfresh_hr_update_Removed.mail_template_notification_hr_expense')
                self.env['mail.template'].browse(mail_template.id).send_mail(template.id, force_send=True, raise_exception=True)

    def get_next_date(self, old_date, tmpl):
        if tmpl.occurrence_type == 'weekly':
            next_date = old_date + timedelta(days=(tmpl.occurrence_period * 7))
            return next_date
        elif tmpl.occurrence_type == 'monthly':
            next_date = old_date + relativedelta(months=tmpl.occurrence_period)
            return next_date
        elif tmpl.occurrence_type == 'annual':
            next_date = old_date + relativedelta(months=(tmpl.occurrence_period * 12))
            return next_date


