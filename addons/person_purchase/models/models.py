
from odoo import models, fields, api
class person_purchase(models.Model):
    _name = 'person.purchase'
    _description ="Person Purchase"
    name =  fields.Char("Person Purchas",default="PR")
    categ_id = fields.Many2one("product.public.category",string="Category")
    person_lines = fields.One2many("person.purchase.line","person_purchase_id",string="Lines")
class address_book(models.Model):
    _name="person.purchase.line"
    person_purchase_id = fields.Many2one("person.purchase")
    categ_id = fields.Many2one(related='person_purchase_id.categ_id', string="Category")
    product_id = fields.Many2one("product.product",string="Product",domain="[('type_pro','=','vegetables and fruits'),('public_categ_ids','=',categ_id)]",copied=True)
    purchase_price = fields.Float("Purchase Price")
    is_published =fields.Boolean(related='product_id.is_published')


    @api.constrains("product_id","purchase_price")
    def save_last_purchase(self):

        #('product_id','=',self.product_id.id)
        price_item = self.env['product.pricelist.item'].search(['|',('product_id','=',self.product_id.id),('product_tmpl_id','=',self.product_id.product_tmpl_id.id)])
        print(price_item)
        for rec in price_item:
            if rec.product_id == self.product_id and rec.product_id:
                 rec.update_price = self.purchase_price
            elif rec.product_tmpl_id==self.product_id.product_tmpl_id and rec.product_tmpl_id:
                rec.update_price = self.purchase_price


        self.product_id.update_price = self.purchase_price
