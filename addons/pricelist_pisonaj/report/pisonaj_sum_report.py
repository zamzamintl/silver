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
        for record in pricelis.item_ids:
            for rec in record.product_tmpl_id.public_categ_ids:
                if rec not in product_cate and rec:
                    product_cate.append(rec)

        cate_id=[]
        pages.append(j)
        print("**********8",product_cate)
        lines=self.env['product.pricelist.item'].search([('pricelist_id','in',pricelis.ids)],order="product_tmpl_id asc")

        for record in product_cate:
            i=0

            count=0
            for lst in pricelis.item_ids:
                if record.id in  lst.product_tmpl_id.public_categ_ids.ids and lst.product_tmpl_id.is_published==True:
                    count+=1

            print("&&&&&&&&&&&",count)
            if count<=24:
                cate_id.append({'page': j, 'cat': record,'check':False,'name':record.name})
            elif count>24:
                cate_id.append({'page': j, 'cat': record, 'check': True,'name':record.name})

            for rec in lines:
                if record.id in  rec.product_tmpl_id.public_categ_ids.ids and rec.product_tmpl_id.is_published==True:
                    if count<=24:
                        docs.append(
                            {'page': j,'product_name':rec.product_tmpl_id.name, 'pro_id':rec.product_tmpl_id,'categ_id':rec.product_tmpl_id.public_categ_ids, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.price})
                    else:
                         if i<=48:
                            if j not in pages:
                                pages.append(j)
                            if i<=24:
                                docs_right.append(
                                    {'page': j, 'product_name':rec.product_tmpl_id.name, 'pro_id':rec.product_tmpl_id,'categ_id':rec.product_tmpl_id.public_categ_ids,'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.price})
                            elif i>24:
                                docs_left.append(
                                    {'page': j,'product_name':rec.product_tmpl_id.name, 'pro_id':rec.product_tmpl_id, 'categ_id':rec.product_tmpl_id.public_categ_ids,'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.price})

                         else:
                            j += 1
                            pages.append(j)
                            i = 0
                            cate_id.append({'page': j, 'cat': record,'check': True,'name':record.name})

                         i+=1
            j+=1
        website_logo=[]
        if len(pricelis)==1:
           website_logo = pricelis.website_id
        height_field=1
        height=[]
        docs_left = sorted(docs_left, key=lambda i: i['product_name'])
        docs_right = sorted(docs_right, key=lambda i: i['product_name'])
        docs = sorted(docs, key=lambda i: i['product_name'])
        cate_id = sorted(cate_id, key=lambda i: i['name'])
        print(cate_id)
        print(docs)
        print(docs_right)
        print(docs_left)

        return {
            # 'doc_ids': docs.ids,
            'doc_model': 'product.pricelist',
            'docs_left': docs_left,
            'docs_right':docs_right,
            'docs':docs,
            'height_field':height_field,
            'check':check,
            'pages':pages,
            'website_logo':website_logo,
            'product_cate':product_cate,
            'cate_id':cate_id,
            'proforma': True
        }
