from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'
    puchase_price= fields.Float("Price of Purchase ",readonly=True,store=False)
    amount_list= fields.Selection([('Precentage','Precentage'),('Amount','Amount')],'Type')
    amount= fields.Float("Amount")
    precentage= fields.Float("Precentage")
    compute_price = fields.Selection([
        ('fixed', 'Fixed Price'),
        ('percentage', 'Percentage (discount)'),
        ('formula', 'Formula'),('Purchase Price', 'Purchase Price')], index=True, default='fixed', required=True)
    @api.onchange('product_tmpl_id')
    def _get_last_purchase_price(self):
        if self.product_tmpl_id:
            purchase_order_line = self.env['purchase.order.line'].search([('state','=','purchase'),('product_id.product_tmpl_id','=',self.product_tmpl_id.id)],order ='write_date desc')
            print("*******************",purchase_order_line)
            if purchase_order_line:
               print( purchase_order_line.product_id.name)

               self.puchase_price=purchase_order_line[0].price_unit
               print(self.puchase_price)
            else:
               self.puchase_price=0
    @api.onchange("amount_list","precentage","amount")
    def get_changes(self):

        if self.amount_list=='Precentage':
            print(self.amount_list)

            self.price=((self.puchase_price*self.precentage)/100)+self.puchase_price

            print(self.price)
        if  self.amount_list=='Amount':
            print(self.amount_list)
            self.price=self.puchase_price+self.amount
            print(self.price)




