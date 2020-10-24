from datetime import datetime
import logging
from odoo import fields, http, tools, _,models,api

# class AccountMove(models.Model):
#     _inherit = 'account.move'
#     employee_id = fields.Many2one('hr.employee', string='Employee Name')


class Payment(models.Model):
    _inherit='account.payment'
    doc_attachment = fields.Many2many('ir.attachment', 'doc_attach_rel', 'doc_id', 'attach_id3', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    payment_value = fields.Selection([('Cash','Cash'),('Cheque','Cheque')],string='Payment',default='Cash')
    value_date = fields.Date("Value Date")
    bank_name = fields.Char("Bank Name")
    cheque_no = fields.Char("Cheque No")
    cheq_partner_type = fields.Selection([('customer','customer'),('supplier','vendor'),('Employee','Employee')],string="Partner Type",default='customer')
    employee_id = fields.Many2one('hr.employee',string='Employee Name')
    account_id =fields.Many2one('account.account',string="Account Name")
    Analtyical_account = fields.Many2one('account.analytic.account',string='Analtyical Account')
    Analtyical_tag = fields.Many2one('account.analytic.tag',string='Analtyical Tag')


    _sql_constraints = [
        ('cheque_no', 'UNIQUE (cheque_no)', 'Cheque Number must be unique')
    ]

    @api.onchange('cheq_partner_type')
    def get_partner_type(self):
        if self.cheq_partner_type=='supplier' or self.cheq_partner_type=='customer':
            self.partner_type=self.cheq_partner_type
    def post_employ(self):
        lines,tag=[],[]
        part_id=''
        self.name = "Emp/"+str(datetime.now().year)+"/"+str(self.id)
        if self.employee_id.user_id:
            part_id = self.employee_id.user_id.partner_id.id
        move2 = self.env['account.move'].create({'date': self.payment_date,
                                                 'name':'',

                                                 'ref': self.cheque_no or '',
                                                 'company_id': self.company_id.id,
                                                 'journal_id': self.journal_id.id,

                                                 })
        if self.Analtyical_tag:
            tag=[(4, self.Analtyical_tag.id)]
        if self.payment_type=='outbound':
            lines.append((0,0, {
                'account_id': self.account_id.id,
                'analytic_account_id':self.Analtyical_account.id or '',
                'partner_id': part_id,
                'debit': self.amount,
                'credit': 0,
                'payment_id':self.id,
                'move_id':move2.id
            }))
            lines.append((0, 0, {
                'account_id': self.journal_id.default_credit_account_id.id,
                'analytic_account_id': self.Analtyical_account.id or '',
                'partner_id': part_id,
                'debit': 0,
                'credit': self.amount,
                'payment_id': self.id,
                'move_id': move2.id
            }))
        if self.payment_type=='inbound':
            lines.append((0,0, {
                'account_id': self.account_id.id,
                'analytic_account_id':self.Analtyical_account.id or '',
                'partner_id': part_id,
                'debit': 0,
                'credit': self.amount,
                'payment_id':self.id,
                'move_id': move2.id
            }))
            lines.append((0, 0, {
                'account_id': self.journal_id.default_credit_account_id.id,
                'analytic_account_id': self.Analtyical_account.id or '',
                'partner_id': part_id,
                'debit': self.amount,
                'credit': 0,
                'payment_id': self.id,
                'move_id': move2.id
            }))
        self.move_line_ids=lines
        move2.write({'line_ids':self.move_line_ids,'state':'posted'})

        self.state='posted'



    def write(self,values):

        if self.move_line_ids:
            for rec in self.move_line_ids:

                if self.Analtyical_account:
                     rec.analytic_account_id = self.Analtyical_account.id
                if self.Analtyical_tag:
                   rec.analytic_tag_ids = [(4,self.Analtyical_tag.id)]
        return super(Payment,self).write(values)






