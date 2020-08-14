import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
class productemplate(models.Model):
    _inherit = 'product.template'
    type_pro = fields.Selection([('vegetables and fruits', 'vegetables and fruits'), ('juice', 'juice')], string='Sub Type')

class product(models.Model):
    _inherit='product.product'

    sale_amount=fields.Float(compute='_get_sale_order',String="Sale Count",default=0)
    type_pro =fields.Selection(related='product_tmpl_id.type_pro',string='Sub Type')
    #type_pro =fields.Selection([('vegetables and fruits','vegetables and fruits'),('juice','juice')],string='type')
    purchase_amount=fields.Float(compute='_get_purchase_order',String="Sale Amount")
    @api.depends("sales_count")
    def _get_sale_order(self):
        products=self.env['product.product'].search([])
        
        for pro in products:
            q,p=0,0
            if pro.sales_count>0:
                
                sale_order=self.env["sale.order.line"].search([('product_id','=',pro.id)])
                for rec in sale_order:
                    
                    p+=rec.price_subtotal
                
            pro.sale_amount=p 
    @api.depends("purchased_product_qty")
    def _get_purchase_order(self):
        products=self.env['product.product'].search([])
        
        for pro in products:
            q,p=0,0
            if pro.purchased_product_qty>0:
                
                sale_order=self.env["purchase.order.line"].search([('product_id','=',pro.id)])
                for rec in sale_order:
                    
                    p+=rec.price_subtotal
                
            pro.purchase_amount=p


class productemplate(models.Model):
    _inherit = 'product.template'
    type_pro = fields.Selection([('vegetables and fruits', 'vegetables and fruits'), ('juice', 'juice')], string='Sub Type')
