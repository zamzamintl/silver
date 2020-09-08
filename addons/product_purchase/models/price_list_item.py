from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_repr

class PricelistItem(models.Model):
    _inherit = 'product.pricelist.item'
    puchase_price= fields.Float("Price of Purchase ",store=False,compute='_get_last_purchase_price')
    amount_list= fields.Selection([('Precentage','Precentage'),('Amount','Amount')],'Type')
    amount= fields.Float("Amount")
    precentage= fields.Float("Precentage")
    compute_price = fields.Selection([
        ('fixed', 'Fixed Price'),
        ('percentage', 'Percentage (discount)'),
        ('formula', 'Formula'),('Purchase Price', 'Purchase Price')], index=True, default='fixed', required=True)
    @api.depends('product_tmpl_id')
    def _get_last_purchase_price(self):
        for rec in self:
            if rec.product_tmpl_id:
                purchase_order_line = rec.env['purchase.order.line'].search([('state','=','purchase'),('product_id.product_tmpl_id','=',rec.product_tmpl_id.id)],order ='write_date desc')

                if purchase_order_line:

                   rec.puchase_price=purchase_order_line[0].price_unit
                else:
                    rec.puchase_price = 0


            else:
               rec.puchase_price=0

    @api.depends('applied_on', 'categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
                 'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge',"amount_list","precentage","amount")
    def _get_pricelist_item_name_price(self):
        for item in self:
            if item.categ_id and item.applied_on == '2_product_category':
                item.name = _("Category: %s") % (item.categ_id.display_name)
            elif item.product_tmpl_id and item.applied_on == '1_product':
                item.name = _("Product: %s") % (item.product_tmpl_id.display_name)
            elif item.product_id and item.applied_on == '0_product_variant':
                item.name = _("Variant: %s") % (item.product_id.with_context(display_default_code=False).display_name)
            else:
                item.name = _("All Products")

            if item.compute_price == 'fixed':
                decimal_places = self.env['decimal.precision'].precision_get('Product Price')
                if item.currency_id.position == 'after':
                    item.price = "%s %s" % (
                        float_repr(
                            item.fixed_price,
                            decimal_places,
                        ),
                        item.currency_id.symbol,
                    )
                else:
                    item.price = "%s %s" % (
                        item.currency_id.symbol,
                        float_repr(
                            item.fixed_price,
                            decimal_places,
                        ),
                    )
            elif item.compute_price == 'percentage':
                item.price = _("%s %% discount") % (item.percent_price)
            elif item.amount_list=='Precentage':
                item.price=((item.puchase_price*item.precentage)/100)+item.puchase_price



            elif  item.amount_list=='Amount':
                item.price=item.puchase_price+item.amount
                print(item.price)
            else:
                item.price = _("%s %% discount and %s surcharge") % (item.price_discount, item.price_surcharge)








