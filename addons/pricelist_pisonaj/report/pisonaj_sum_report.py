from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz

import math
import operator
from collections import OrderedDict
from collections import OrderedDict
_logger = logging.getLogger(__name__)


class ReportProductSale(models.AbstractModel):
    _name = "report.pricelist_pisonaj.pisonaj_sum_report"

    def _get_report_values(self, docids, data=None):
        docs_right,docs_left,docs=[],[],[]
        pricelis =self.env['product.pricelist'].search([('id','in',docids)])
        i,j=1,1
        pages=[]
        check=False

        product_cate=[]
        for rec in pricelis.item_ids:
            if rec.product_tmpl_id.categ_id not in product_cate and rec.product_tmpl_id.categ_id :
                product_cate.append(rec.product_tmpl_id.categ_id)

        cate_id=[]
        pages.append(j)
        for record in product_cate:
            i=0

            count=0
            for lst in pricelis.item_ids:
                if record.id == lst.product_tmpl_id.categ_id.id:
                    count+=1

            print("&&&&&&&&&&&",count)
            if count<=30:
                cate_id.append({'page': j, 'cat': record,'check':False})
            else:
                cate_id.append({'page': j, 'cat': record, 'check': True})

            for rec in pricelis.item_ids:
                if record.id == rec.product_tmpl_id.categ_id.id:
                    if count<=30:
                        docs.append(
                            {'page': j,'pro_id':rec.product_tmpl_id,'categ_id':rec.product_tmpl_id.categ_id, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
                    else:
                         if i<=60:
                            if j not in pages:
                                pages.append(j)
                            if i % 2 == 0:
                                docs_right.append(
                                    {'page': j, 'pro_id':rec.product_tmpl_id,'categ_id':rec.product_tmpl_id.categ_id,'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
                            else:
                                docs_left.append(
                                    {'page': j,'pro_id':rec.product_tmpl_id, 'categ_id':rec.product_tmpl_id.categ_id,'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})

                         else:
                            j += 1
                            pages.append(j)
                            i = 0
                            cate_id.append({'page': j, 'cat': record,'check': True})

                i+=1
            j+=1


        print("++++++++++++++++++++++++++++++++***********",cate_id)
        print(docs)
        print(pages)
        print(docs_left)
        print(docs_right)
        height_field=1
        height=[]
        if len(pricelis.item_ids) >= 30:
            check = True
            height_field = math.ceil(i/29)


        return {
            # 'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs_left': docs_left,
            'docs_right':docs_right,
            'docs':docs,
            'height_field':height_field,
            'check':check,
            'pages':pages,
            'product_cate':product_cate,
            'cate_id':cate_id,
            'proforma': True
        }
