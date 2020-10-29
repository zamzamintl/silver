
from odoo import models, fields, api
import datetime
class Invoice (models.Model):
    _inherit = 'account.move'
    def remove_invoice(self):
         self.name='/'
         self.state='draft'
         domain = [('type', '=', self.type)]
         self.unlink()

         view = self.env.ref('account.view_invoice_tree')

         return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_type': 'form',
            'domain': domain,
            'view_mode': 'tree,form',
            'target': '',
        }
        #  return {
        #     'name': ('Invoices'),
        #     'view_mode': 'form',
        #     'view_id': view.id,
        #     'res_model': 'account.move',
        #     'type': 'ir.actions.act_window',
        #      'domain':domain,
        #
        #     'target': 'current'
        # }

        # sql="delete from account_move where id = %s"%(self.id)
        # self._cr.execute(sql)
class Payment (models.Model):
    _inherit = 'account.payment'
    def remove_payment(self):
         domain = [('payment_type', '=', self.payment_type)]
         self.action_draft()
         sql="delete from account_payment where id = %s"%(self.id)
         self._cr.execute(sql)
         view = self.env.ref('account.view_account_payment_treem')
         return {
             'type': 'ir.actions.act_window',
             'name': 'Payment',
             'res_model': 'account.payment',
             'view_type': 'form',
             'domain': domain,
             'view_mode': 'tree,form',
             'target': '',
         }

         # return {
         #     'name': ('Payment'),
         #     'view_mode': 'form',
         #     'view_id': view.id,
         #     'res_model': 'account.payment',
         #     'type': 'ir.actions.act_window',
         #      'domain':domain,
         #     'target': 'current'
         # }

