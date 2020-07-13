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
    _name = "report.sales_sum.saleorder_sum_report"
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
              
         
        product_list=[]
        customer_list,cst=[],[]
        sales_rep_list=[]
        ids=[]
        sales_rep=''
        
        for rec in docs.order_line:
            ids.append(rec.order_id.id)
            product_list.append(rec.product_id.id)
            sales_rep_list.append(rec.order_id.user_id.id)
        sales_orders=self.env['sale.order'].search([('id','in',ids)],order='id asc')
        sales_rep_list=list(OrderedDict.fromkeys(sales_rep_list))
        if len(sales_rep_list)==1:
            sales_rep=self.env['res.users'].search([('id','=',sales_rep_list)]).name
        
        for rlt in sales_orders:
            partner_id=rlt.partner_id
            address=""
            if partner_id.street:
                address+=partner_id.street+"-"
            if partner_id.city:
                address+=partner_id.city+"-"+partner_id.state_id.name
            if partner_id.state_id:
                address+=partner_id.state_id.name

            cst.append({'id':rlt.id,'address':address,'name':partner_id.name,'phone':partner_id.phone,'SO':rlt.name,'total':rlt.amount_total})
         
         
        product_list=list(OrderedDict.fromkeys(product_list))
        list_qty=[]
        for pro in product_list:
            qty=0
            so=''
            pro_name=self.env['product.product'].search([('id','=',pro)])
            if pro_name.type!='service':
                for order in docs.order_line:
                    if pro ==order.product_id.id :
                        qty+=order.product_uom_qty
                        so+=order.order_id.name+"  "
                list_qty.append({'product':pro_name.name,'qty':qty})
        _logger.info(list_qty)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'list_qty':list_qty,
            'cst':cst,
            'sales_rep':sales_rep,
            'proforma': True
        }