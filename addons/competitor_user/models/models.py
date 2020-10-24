
from odoo import models, fields, api
import datetime
class person_competitor(models.Model):
    _name = 'person.competitor'
    _description ="Person competitor"
    name =  fields.Char("name",default="PR",compute='get_name')
    creation_date = fields.Date("Creation Date", default=lambda self: fields.datetime.now().date())
    competitor_id = fields.Many2one("res.competitor",string="competitor")
    person_lines = fields.One2many("person.competitor.line","person_competitor_id",string="Lines")
    categ_id =  fields.Many2many("product.public.category","comp_cate_pro","com_id",string="Category")
    products = fields.Many2many("product.product", "pro_comp", 'id_comp', compute='get_list_products', store=True)

    @api.depends("person_lines")
    def get_list_products(self):
        self.products = []
        for rec in self.person_lines:
            pro = rec.product_id.id
            if pro:
                self.products = [(4, pro)]
    @api.depends("competitor_id")
    def get_name(self):
        if self.competitor_id:
            self.name=self.competitor_id.name
class address_book(models.Model):
    _name="person.competitor.line"
    person_competitor_id = fields.Many2one("person.competitor")
    categ_id = fields.Many2many(related='person_competitor_id.categ_id',string="Category ")
    #product_ids = fields.Many2many(related='person_competitor_id.product_ids')
    product_id = fields.Many2one("product.product",string="Product",auto_join=True,required="1")
    published = fields.Boolean(related='product_id.is_published',string="publish")
    competitor_price = fields.Float("competitor Price",required="1")
    my_price = fields.Float(related='product_id.lst_price')
    creation_date = fields.Date(related='person_competitor_id.creation_date',string="Creation Date")
    products = fields.Many2many(related='person_competitor_id.products')

    @api.onchange('product_id')
    def get_domain(self):

        ids = []
        for rec in self.products:
            # if rec.public_categ_ids == self.categ_id.id and rec.type_pro=='vegetables and fruits':

            ids.append(rec._origin.id)
        domain = []
        print("ids", ids)
        if ids:
            cat_ids = []
            for rec in self.categ_id:
                cat_ids.append(rec._origin.id)
            return {
                'domain': {'product_id': [('id', 'not in', ids),
                                          ('public_categ_ids', '=', cat_ids)]}
            }
        # ('type_pro', '=', 'vegetables and fruits'),
        if self.categ_id:
            cat_ids=[]
            for rec in self.categ_id:
                cat_ids.append(rec._origin.id)
            return {
                'domain': {'product_id': [('public_categ_ids', 'in', cat_ids)]}
            }



class competitor(models.Model):
    _name = 'res.competitor'
    name = fields.Char("Name" ,required="1")
    region_id = fields.Many2one("state.region1","Region")
    #website = fields.Char("Website")
    categ_competitor = fields.Many2one("res.competitor.category",string='Category')
class category_competitor(models.Model):
    _name = 'res.competitor.category'
    name = fields.Char("Name")



