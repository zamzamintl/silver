
from odoo import models, fields, api

class address_book(models.Model):
    _name="person.purchase"
    product_id = fields.Many2one("product.product",string="Product",domain=[('type_pro','=','vegetables and fruits')])
    purchase_price = fields.Float("Purchase Price")
    @api.constrains("product_id","purchase_price")
    def save_last_purchase(self):

        self.product_id.update_price = self.purchase_price
