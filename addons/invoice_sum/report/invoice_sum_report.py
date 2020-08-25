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
        print("get_reprort incoive ++++++++++++++++++++++++++++")
        move =self.env['account.move'].search([('id','in',docids)])
        docs=[]

        cst_list=[]
        for record in move.invoice_line_ids:
                if record.move_id not in cst_list:
                    cst_list.append(record.move_id.partner_id)
                print(record)
                res = self.search_docs(docs,record.product_id)
                print(res)
                if res ==False:
                    docs.append({'product_id':record.product_id,'price_unit':record.price_unit,'quantity':record.quantity
                                    ,"tax_ids":record.tax_ids,"price_total":record.price_subtotal,'check':False})
                else:
                    for item in docs:
                        if item["product_id"] ==record.product_id and item["price_unit"] ==record.price_unit:
                                    item["quantity"]+=record.quantity
                                    item["price_total"] += record.price_subtotal
                        elif item["product_id"] ==record.product_id and item["price_unit"] !=record.price_unit:
                                    docs.append(
                                    {'product_id': record.product_id, 'price_unit': record.price_unit, 'quantity': record.quantity
                                        , "tax_ids": record.tax_ids, "price_total": record.price_subtotal})
        print(docs)

        return {
            # 'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs': docs,
            'cst_list':cst_list,
            'move':move,

            'proforma': True
        }
    def search_docs(self, docs, product_id):
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%555")
            print(docs)
            if len(docs)==0:
                return False
            else:
               for item in docs:
                    if item["product_id"] == product_id:
                        return True
                    else:
                        return False



