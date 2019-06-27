# -*- coding: utf-8 -*-
"""
    Author: Tobias Reinwarth (tobias.reinwarth@manatec.de)
    Copyright: 2019, manaTec GmbH
    Date created: 25.01.19
"""

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    DESCRIPTION_FIELD_NAME = 'name'
    HELPDESK_TICKET_FIELD_NAME = 'helpdesk_ticket_id'

    @api.multi
    def write(self, vals):
        if self.DESCRIPTION_FIELD_NAME in vals and vals.get(self.DESCRIPTION_FIELD_NAME) and self.helpdesk_ticket_id:
            vals.update({self.DESCRIPTION_FIELD_NAME: '%s | #%s' % (vals.get(self.DESCRIPTION_FIELD_NAME), self.helpdesk_ticket_id.id)})

        super(AccountAnalyticLine, self).write(vals)

    @api.model
    def create(self, vals):
        if self.DESCRIPTION_FIELD_NAME in vals and vals.get(self.DESCRIPTION_FIELD_NAME) and self.HELPDESK_TICKET_FIELD_NAME in vals:
            vals.update({self.DESCRIPTION_FIELD_NAME: '%s | #%s' % (vals.get(self.DESCRIPTION_FIELD_NAME), vals.get(self.HELPDESK_TICKET_FIELD_NAME))})

        return super(AccountAnalyticLine, self).create(vals)
