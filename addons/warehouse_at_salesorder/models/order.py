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


        
        for pro in product_list:
            q=0
            for order in self.sales_order:
                for line in order.order_line:


                    if pro.id==line.product_id.id:
                        q+=line.product_uom_qty
            bom_id = self.env['mrp.bom'].search(['|',('product_id','=',pro.id),('product_tmpl_id', '=', pro.product_tmpl_id.id)],
                                                order='write_date desc', limit=1)
            if bom_id:
                stock_qty = self.env['stock.quant'].search([('product_id', '=', pro.id),
                                                            ('on_hand', '=', True),
                                                            ('location_id', '=', self.warehouse_id.lot_stock_id.id)])
                bom_qty_available = q-stock_qty.quantity
                print("bom qty",bom_qty_available)
                print("bom qty",q)
                print("bom qty",stock_qty.quantity)
                for rec in bom_id.bom_line_ids:

                    stock_qty = self.env['stock.quant'].search([('product_id', '=', rec.product_id.id),
                                                            ('on_hand', '=', True),
                                                            ('location_id', '=', self.warehouse_id.lot_stock_id.id)])
                    print(rec.product_id.name)
                    print(stock_qty.quantity)
                    print(rec.product_qty)
                    print(bom_qty_available)


                    q_requested = (bom_qty_available*rec.product_qty)- stock_qty.quantity

                    if q_requested < 0:
                        q_requested = 0

                    if q_requested > 0:
                        lines.append({'product_id': rec.product_id.id, "product_qty": q_requested , "product_uom": rec.product_id.uom_id.id,
                                      'name': rec.product_id.name, 'date_planned': datetime.now()})


            else:
                stock_qty=self.env['stock.quant'].search([('product_id','=',pro.id),
                                                          ('on_hand','=',True),('location_id','=',self.warehouse_id.lot_stock_id.id)])

                q_requested=q-stock_qty.quantity


                if q_requested<0:
                    q_requested=0

                if q_requested > 0:

                    lines.append({'product_id':pro.id,"product_qty":q_requested,"product_uom":pro.uom_id.id,'name':pro.name,'date_planned':datetime.now()})

        purchase_order=self.env['purchase.order']
        picking_type=self.env['stock.picking.type'].search([('code','=','incoming'),('defualt_warhouse_purchase','=',True)])
        picking_type_id=0
        vendor = self.env['res.partner'].search([('default_purchase_oer','=',True)]).id
        for rec in picking_type:
                picking_type_id=rec.id
                break
        return{ 'name':'Purchase order',
            'res_model': 'purchase.order',
            'target': 'new',
             'view_type': 'form',
             'view_mode': 'form',
            'view_id':self.env.ref('purchase.purchase_order_form').id ,
             
            'context':{'default_order_line':lines,'default_picking_type_id':picking_type_id,'default_partner_id':vendor},
            'type': 'ir.actions.act_window',}


class stock_warhouse(models.Model):
     _inherit = 'stock.warehouse'
     defualt_warhouse = fields.Boolean("default warehouse ",default=False)
class Picking (models.Model):
    _inherit = 'stock.picking.type'
    defualt_warhouse_purchase = fields.Boolean("default warehouse Purchase",default=False)

