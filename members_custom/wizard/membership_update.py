# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class MembershipUpdate(models.Model):
    _name = 'membership.update'
    _rec_name = 'partner_id'
    _description = 'Membership Update'

    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    old_membership_id = fields.Many2one(comodel_name="membership.membership_line", string="Old Membership")

    def action_open_new_membership(self):
        if self.old_membership_id:
            inv_id = self.old_membership_id.account_invoice_id
            if inv_id:
                payment_ids = inv_id.payment_ids
                for payment in payment_ids:
                    print(payment.move_line_ids)
                    payment.move_line_ids.with_context(invoice_id=inv_id.id).remove_move_reconcile()
                inv_id.move_id.journal_id.update_posted = True
                inv_id.action_invoice_cancel()
                self.old_membership_id.with_context(allow_membership_line_unlink=True).unlink()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Membership Invoice'),
            'res_model': 'membership.invoice',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {
                'active_ids': self.partner_id.id
            },
        }
