from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz
import operator
from collections import OrderedDict
from collections import OrderedDict
_logger = logging.getLogger(__name__)


class ReportProductSale(models.AbstractModel):
    _name = "report.invoice_sum.invoice_sum_report"

    def _get_report_values(self, docids, data=None):
        #print("get_reprort incoive ++++++++++++++++++++++++++++")
        move =self.env['account.move'].search([('id','in',docids)])
        docs=[]

        cst_list=[]
        for rec in move:
            for record in rec.invoice_line_ids:
                if record.move_id not in cst_list:
                    cst_list.append(record.move_id.partner_id)

                res = self.search_docs(docs,record.product_id,rec)

                if res ==False:
                    docs.append({'move_id':rec,'product_id':record.product_id,'price_unit':record.price_unit,'quantity':record.quantity
                                    ,"tax_ids":record.tax_ids,"price_total":record.price_subtotal,'check':False})
                else:
                    for item in docs:

                        if item["product_id"] ==record.product_id and item["price_unit"] ==record.price_unit and item['move_id']==rec:
                                    item["quantity"]+=record.quantity
                                    item["price_total"] += record.price_subtotal
                        elif item["product_id"] ==record.product_id and item["price_unit"] !=record.price_unit  and item['move_id']==rec:
                                    docs.append(
                                    {'move_id':rec,'product_id': record.product_id, 'price_unit': record.price_unit, 'quantity': record.quantity
                                        , "tax_ids": record.tax_ids, "price_total": record.price_subtotal})


        return {
            # 'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs': docs,
            'cst_list':cst_list,
            'move':move,

            'proforma': True
        }
    def search_docs(self, docs, product_id,move_id):
            check=False
            if len(docs)==0:
                print("first")
                return False
            else:
               for item in docs:
                    print(item)
                    print(item['product_id'])

                    if item["product_id"] == product_id and item['move_id']==move_id:
                        check=True
                        return True
               if check==False:
                        return False



