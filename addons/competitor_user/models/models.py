
from odoo import models, fields, api
import datetime
class person_competitor(models.Model):
    _name = 'person.competitor'
    _description ="Person competitor"
    name =  fields.Char("name",default="PR",compute='get_name')
    creation_date = fields.Date("Creation Date", default=lambda self: fields.datetime.now().date())
    competitor_id = fields.Many2one("res.competitor",string="competitor")
    person_lines = fields.One2many("person.competitor.line","person_competitor_id",string="Lines")
    @api.depends("competitor_id")
    def get_name(self):
        if self.competitor_id:
            self.name=self.competitor_id.name
class address_book(models.Model):
    _name="person.competitor.line"
    person_competitor_id = fields.Many2one("person.competitor")

    product_id = fields.Many2one("product.product",string="Product",auto_join=True)
    published = fields.Boolean(related='product_id.is_published',string="publish")
    competitor_price = fields.Float("competitor Price")
    my_price = fields.Float(related='product_id.lst_price')
    creation_date = fields.Date(related='person_competitor_id.creation_date',string="Creation Date")
    # product_ids = fields.Many2many("product.product", string="Product",compute='_get_domain')
    #
    #
    # @api.depends("product_id")
    # def _get_domain(self):
    #     if self.product_id:
    #         self.product_ids=[(4,self.product_id.id)]
    #     print("oooo",self.product_ids)
    # def unlink(self):
    #     if self.product_id:
    #         self.product_ids = [(3, self.product_id)]
    #     return super(address_book, self).unlink()
            
            


class competitor(models.Model):
    _name = 'res.competitor'
    name = fields.Char("Name")
    region_id = fields.Many2one("state.region1","Region")
    website = fields.Char("Website")
class category_competitor(models.Model):
    _name = 'res.competitor.category'
    name = fields.Char("Name")



