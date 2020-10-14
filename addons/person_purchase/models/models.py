
from odoo import models, fields, api
class person_purchase(models.Model):
    _name = 'person.purchase'
    _description ="Person Purchase"
    name =  fields.Char("Person Purchas",default="PR")
    categ_id = fields.Many2one("product.public.category",string="Category")
    person_lines = fields.One2many("person.purchase.line","person_purchase_id",string="Lines")
    products = fields.Many2many("product.product", "pro", 'id', compute='get_list_products')

    @api.depends("person_lines")
    def get_list_products(self):
        for rec in self.person_lines:
            pro = rec.product_id.id
            print(pro)
            self.products = [(4, pro)]
        print("oooo", self.products)
class address_book(models.Model):
    _name="person.purchase.line"
    person_purchase_id = fields.Many2one("person.purchase")
    categ_id = fields.Many2one(related='person_purchase_id.categ_id', string="Category")
    product_id = fields.Many2one("product.product",string="Product")
    purchase_price = fields.Float("Purchase Price")
    is_published =fields.Boolean(related='product_id.is_published')
    products = fields.Many2many("product.product", "pro", 'id')


    # @api.onchange("product_id")
    # def get_domain(self):
    #     pt()
    #     if self.person_purchase_id.products:
    #         ids=[]
    #         for rec in self.person_purchase_id.products:
    #             ids.append(rec.id)
    #             print(rec.id)
    #         return {
    #         'domain': {'product_id': [('id', 'not in', ids)]}
    #     }


    @api.constrains("product_id","purchase_price")
    def save_last_purchase(self):

        #('product_id','=',self.product_id.id)
        for record in self:
            price_item = self.env['product.pricelist.item'].search(['|',('product_id','=',record.product_id.id),('product_tmpl_id','=',record.product_id.product_tmpl_id.id)])
            print(price_item)
            for rec in price_item:
                if rec.product_id == record.product_id and rec.product_id:
                     rec.update_price = record.purchase_price
                elif rec.product_tmpl_id==record.product_id.product_tmpl_id and rec.product_tmpl_id:
                    rec.update_price = record.purchase_price


            record.product_id.update_price = record.purchase_price
