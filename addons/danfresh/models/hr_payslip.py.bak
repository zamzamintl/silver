# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Pay Slip'

    @api.multi
    def action_payslip_cancel(self):
        if self._fields.get('move_id'):
            self.journal_id.update_posted=True

            self.move_id.button_cancel()
            self.move_id.unlink()
        return self.write({'state': 'cancel'})
