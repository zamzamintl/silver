
from odoo import api, fields, models


class PeriodicalReportProduct(models.TransientModel):
    _name = "customer.statement"

     
    date_from = fields.Date(string='تاريخ البدء')
    date_to = fields.Date(string='تاريخ الانتهاء')
    customer=fields.Many2many('res.partner','user_id','id',string='العميل')
    check=fields.Boolean(default=False,string='العميل')

  
    def check_report(self):
        list=[] 
        for rec in self.customer:
            list.append(rec.id)
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'customer':list,
                'check':self.check

            },
        }
        return self.env.ref('customer_statement.action_report_customer_statement').report_action(self, data=data)
