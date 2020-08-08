
from collections import OrderedDict
from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz
_logger = logging.getLogger(__name__)


class ReportPeriodicalSale(models.AbstractModel):
    _name = 'report.product_qty_inventory.report_product_qty_inventory'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        pro = data['form']['product']

        total_sale = 0.0
        period_value = ''
        domain = []
        if pro :
            domain.append([('product_id','=',pro)])
        stock_moves = self.env['stock.move'].search(
            domain, order='date,product_id asc')

        moves = []
        order_line = []
        ids=[]
        dates=[]
        if date_from:
           date_from=datetime.datetime.strptime(date_from, '%Y-%m-%d')
        if date_to:
            date_to=datetime.datetime.strptime(date_to, '%Y-%m-%d')

        old_timezone = pytz.timezone("UTC")
        new_timezone = pytz.timezone("Africa/Cairo")

        _logger.info('STOKE MOVE')
        note_sale = ''

        ids=[]
        old_timezone = pytz.timezone("UTC")
        new_timezone = pytz.timezone("Africa/Cairo")
        product_list=[]
        if date_to or date_from:
            for rec in stock_moves:
                if rec.product_id not in product_list:
                    product_list.append(rec.product_id)
                last_new_timezone = old_timezone.localize(rec.date).astimezone(new_timezone)
                last_new_timezone=last_new_timezone.strftime('%Y-%m-%d')
                last_new_timezone=datetime.datetime.strptime(last_new_timezone, '%Y-%m-%d')
                if date_to and date_from:
                    if date_from<=last_new_timezone and date_to>=last_new_timezone:
                        ids.append(rec.id)
                elif date_from:
                    if date_from<=last_new_timezone:
                        ids.append(rec.id)
                elif date_to:
                    if date_to>=last_new_timezone :
                        ids.append(rec.id)
             
            if ids:
                stock_moves=self.env["stock.move"].search([('id','in',ids)])
            else:
                stock_moves=[]
        return_so,delivery_so,return_po,delivery_po,return_ma,delivery_ma,return_internal,delivery_internal=0,0,0,0,0,0,0,0
        value_list=[]
        i=0
        for product in product_list:
            i+=1
            for rec in stock_moves:
                if rec.product.id == product.id:
                    if rec.locati_id.usage=='customer':
                        return_so+=rec.product_uom_qty
                    elif rec.locati_id.usage=='internal':
                        return_internal+=rec.product_uom_qty
                    elif rec.locati_id.usage == 'supplier':
                       return_po += rec.product_uom_qty
                    elif rec.locati_id.usage=='production':
                        return_ma+=rec.product_uom_qty
                    if rec.location_dest_id.usage=='customer':
                        delivery_so+=rec.product_uom_qty
                    elif rec.location_dest_id.usage=='internal':
                        delivery_internal+=rec.product_uom_qty
                    elif rec.location_dest_id.usage == 'supplier':
                       delivery_po += rec.product_uom_qty
                    elif rec.location_dest_id.usage=='production':
                        delivery_ma+=rec.product_uom_qty
        value_list.append({'i':i,'product_id':product,'return_so':return_so,'delivery_so':delivery_so,'return_internal':return_internal,
                           'delivery_internal':delivery_internal,'return_po':return_po,'delivery_po':delivery_po,'return_ma':return_ma,'delivery_ma':
                           'delivery_ma'})


        if date_from:
           date_from=date_from.strftime('%Y-%m-%d')
        if date_to:
           date_to=date_to.strftime('%Y-%m-%d')
        return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'date_from': date_from,
                'date_to': date_to,
                'moves': value_list,
                'product_name': self.env['product.product'].search([('id', '=', pro)]).name,
                'data_check': False,


            }

