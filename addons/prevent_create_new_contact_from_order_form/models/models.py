from odoo import api, fields, models, osv


class PreventCreateNewContactFromSalesOrderForm(osv.osv.Model):
    _inherit = 'sale.order'


class PreventCreateNewContactFromPurchaseOrderForm(osv.osv.Model):
    _inherit = 'purchase.order'
