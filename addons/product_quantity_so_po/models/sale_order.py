import logging
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError
from odoo.http import request

class sales_ordder(models.Model):
    _inherit = 'sale.order'
    type_pro =fields.Selection([('vegetables and fruits','vegetables and fruits'),('juice','juice'),('other','other')],
                               compute='get_type_order',string='type')
    sub_type = fields.Selection(
        [('vegetables and fruits', 'vegetables and fruits'), ('juice', 'juice'), ('other', 'other')],
        string='SUb type',store=True)
    @api.depends('order_line')
    def get_type_order(self):
       veg, fruit = 0, 0
       for record in self:
           print("&&&&&&&&&&&&&")
           record.type_pro='other'
           for rec in record.order_line:

               if rec.product_id.type_pro=='vegetables and fruits':
                   veg+=1
               elif rec.product_id.type_pro=='juice':
                   fruit+=1
           if veg >= fruit  and veg !=0:
                   record.type_pro ='vegetables and fruits'
           elif veg < fruit:
                   record.type_pro = 'juice'
           record.sub_type = record.type_pro