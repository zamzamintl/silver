from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    puchase_price= fields.Float("Price of Purchase ",compute='_get_last_purchase_price')
    type_cal= fields.Selection([('Cost','Cost'),('Purchase Price','Purchase Price')],'Type',default='Cost')
    amount_list= fields.Selection([('Precentage','Precentage'),('Amount','Amount')],'Type')
    amount= fields.Float("Amount")
    precentage= fields.Float("Precentage")
    @api.depends("purchased_product_qty")
    def _get_last_purchase_price(self):
        for rec in self.search([]):
               purchase_order_line = self.env['purchase.order.line'].search([('state','=','purchase'),('product_id','=',rec.id)],order ='write_date desc')

               if purchase_order_line:

                   rec.puchase_price=purchase_order_line[0].price_unit
               else:
                   rec.puchase_price=0
    @api.onchange("type_cal","amount_list","precentage","amount")
    def get_changes(self):

        if self.type_cal=='Purchase Price' and self.amount_list=='Precentage':

            self.list_price=((self.puchase_price*self.precentage)/100)+self.puchase_price
            print("&&&&&7",self.list_price)

        if self.type_cal=='Purchase Price' and self.amount_list=='Amount':
            self.list_price=self.puchase_price+self.amount
            print("&&&&&7", self.list_price)




