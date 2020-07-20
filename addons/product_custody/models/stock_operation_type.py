from odoo import fields,api,models


class StockOperationType(models.Model):
    _inherit = 'stock.picking.type'

    custody_stock_src_id = fields.Many2one('stock.location')
    custody_stock_dst_id = fields.Many2one('stock.location')
