from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.product'
    puchase_price= fields.Float("Price of Purchase ",compute='_get_last_purchase_price',store=False)
    type_cal= fields.Selection([('Cost','Cost'),('Purchase Price','Purchase Price')],'Type',default='Cost')
    amount_list= fields.Selection([('Precentage','Precentage'),('Amount','Amount')],'Type')
    amount= fields.Float("Amount")
    precentage= fields.Float("Precentage")
    @api.depends('purchased_product_qty')
    def _get_last_purchase_price(self):

        purchase_order_line = self.env['purchase.order.line'].search([('state','=','purchase'),('product_id','=',self.id)],order ='write_date desc')

        if purchase_order_line:
           print( purchase_order_line.product_id.name)

           self.puchase_price=purchase_order_line[0].price_unit
           print(self.puchase_price)
        else:
           self.puchase_price=0
    @api.onchange("type_cal","amount_list","precentage","amount")
    def get_changes(self):

        if self.type_cal=='Purchase Price' and self.amount_list=='Precentage':

            self.list_price=((self.puchase_price*self.precentage)/100)+self.puchase_price


        if self.type_cal=='Purchase Price' and self.amount_list=='Amount':
            self.list_price=self.puchase_price+self.amount




