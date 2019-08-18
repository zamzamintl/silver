# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def create_membership_invoice(self, product_id=None, datas=None):
        self = self.with_context(start_date=datas.get('start_date'))
        invoice_list = super(ResPartner, self).create_membership_invoice(product_id=product_id, datas=datas)
        return invoice_list

    def action_membership_update(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Membership Update'),
            'res_model': 'membership.update',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'default_partner_id': self.id,
                'partner_id': self.id,
            },

        }
