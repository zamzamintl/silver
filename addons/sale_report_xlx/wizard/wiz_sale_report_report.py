
from odoo import api, fields, models


class PeriodicalReportProduct(models.TransientModel):
    _name = "sale.report.xlx"

     
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date to')
    # customer=fields.Many2many('res.partner','user_id','id',string='العميل')
    customer=fields.Many2one('res.partner',string='Customer')
    name= fields.Char("ffffff",default='fff')

  
    def check_report(self):
        list=[] 
        # for rec in self.customer:
        #     list.append(rec.id)
        data = {
            'ids': self.ids,
            'model': self._name,
            'report_name':'dddd',
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
                'name':self.name,
                # 'customer':list
                'customer':self.customer.id


            },
        }

        return self.env.ref('sale_report_xlx.action_report_sale_report_excel').report_action(self, data=data,)
