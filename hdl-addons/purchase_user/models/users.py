from odoo import models, fields, api


class user(models.Model):
    _inherit = 'res.users'
    def create_purchase(self):

        view = self.env.ref('purchase.purchase_order_form')
        return {
            'name': 'Purchase Order',
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'purchase.order',
            'type': 'ir.actions.act_window',
            'target': 'current'
        }
