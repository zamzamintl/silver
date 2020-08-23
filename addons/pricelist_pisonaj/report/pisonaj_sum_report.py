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

        for rec in pricelis.item_ids:


            if i<=30:
                if i % 2 == 0:
                    docs_right.append(
                        {'page': j, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
                else:
                    docs_left.append(
                        {'page': j, 'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})
                docs.append({'page':j,'product_tmpl_id': rec.product_tmpl_id.name, 'fixed_price': rec.fixed_price})

                pages.append(j)
                i=0
                j += 1
            i+=1
        print(len(docs_left))
        height_field=1
        height=[]
        if i > 29:
            # check = True
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
