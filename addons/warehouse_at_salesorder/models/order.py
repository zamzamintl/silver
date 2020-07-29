import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime

class warehouse(models.Model):
    _name="warehouse.sales"
    warehouse_id=fields.Many2one("stock.warehouse",string="WareHouse")
    sales_order=fields.Many2many("sale.order","wh","id",string="Sales order")
    def action_create_po(self):
        _logger.info("PURCHSE")
        product_list,lines=[],[]
        for rec in self.sales_order:
            for line in rec.order_line:
                if line.product_id not in product_list :
                    product_list.append(line.product_id) 

        _logger.info((product_list))
        
        for pro in product_list:
            q=0
            for order in self.sales_order:
                for line in order.order_line:
                    if pro.id==line.product_id.id:
                        q+=line.product_uom_qty
            _logger.info("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            stock_qty=self.env['stock.quant'].search([('product_id','=',pro.id),('on_hand','=',True),('location_id','=',self.warehouse_id.lot_stock_id.id)])
            
            q_requested=q-stock_qty.quantity
            

            if q_requested<0:
                q_requested=0
            if q_requested > 0:
                
                lines.append({'product_id':pro.id,"product_qty":q_requested,"product_uom":pro.uom_id.id,'name':pro.name,'date_planned':datetime.now()})

        purchase_order=self.env['purchase.order']
        picking_type=self.env['stock.picking.type'].search([('code','=','incoming'),('warehouse_id','=',self.warehouse_id.id)])
        picking_type_id=0
        for rec in picking_type:
                picking_type_id=rec.id
                break
        return{ 'name':'Purchase order',
            'res_model': 'purchase.order',
            'target': 'new',
             'view_type': 'form',
             'view_mode': 'form',
            'view_id':self.env.ref('purchase.purchase_order_form').id ,
             
            'context':{'default_order_line':lines,'default_picking_type_id':picking_type_id},
            'type': 'ir.actions.act_window', }

 