from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_sale_product = fields.Integer(String='Total Ordered Products',compute='_total_sales_product',help="total products")
    total_sale_product_qty = fields.Integer(String='Total Ordered Quantity',compute="_compute_total_sales_product_qty",help="total Quantity")

    def _total_sales_product(self):
        for record in self:
            total_sale_product = 0
            lists=[]
            for line in record.order_line:
                if line.product_id in lists:
                    record.total_sale_product = record.total_sale_product
                else:    
                    lists.append(line.product_id)
                    record.total_sale_product = record.total_sale_product+1

    def _compute_total_sales_product_qty(self):
        for record in self:
            total_sale_product_qty = 0
            for line in record.order_line:
                record.total_sale_product_qty += line.product_uom_qty

