# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class MemberInvoice(models.TransientModel):
    _inherit = 'membership.invoice'

    start_date = fields.Date(string="Start Date", default=lambda self: date.today())

    @api.multi
    def membership_invoice(self):
        if self:
            datas = {
                'membership_product_id': self.product_id.id,
                'amount': self.member_price,
                'start_date': self.start_date,
            }
        invoice_list = self.env['res.partner'].browse(self._context.get('active_ids')).create_membership_invoice(
            datas=datas)
        search_view_ref = self.env.ref('account.view_account_invoice_filter', False)
        form_view_ref = self.env.ref('account.invoice_form', False)
        tree_view_ref = self.env.ref('account.invoice_tree', False)

        return {
            'domain': [('id', 'in', invoice_list)],
            'name': 'Membership Invoices',
            'res_model': 'account.invoice',
            'type': 'ir.actions.act_window',
            'views': [(tree_view_ref.id, 'tree'), (form_view_ref.id, 'form')],
            'search_view_id': search_view_ref and search_view_ref.id,
        }

