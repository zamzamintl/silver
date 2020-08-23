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
        pages.append(j)
        for rec in pricelis.item_ids:

            if len(pricelis.item_ids)<=30:
                docs.append(
                    {'page': j, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
            if i<=60:
                if i % 2 == 0:
                    docs_right.append(
                        {'page': j, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
                else:
                    docs_left.append(
                        {'page': j, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})

            else:
                j += 1
                pages.append(j)
                i = 0

            i+=1
        print(docs)
        print(pages)
        print(len(pricelis.item_ids))
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
            'proforma': True
        }
