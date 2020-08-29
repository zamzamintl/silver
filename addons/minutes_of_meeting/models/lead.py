from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)
class lead(models.Model):
    _inherit ='crm.lead'
    count_meeting =fields.Integer("count Meeting")

    def action_view_meeting(self):
        return {
            'name': _('Meeting'),
            'view_mode': 'form',
            'res_model': 'calendar.event',
            'type': 'ir.actions.act_window',
            'domain': [("opportunity_id", "=", self.id)],
            'target': 'current'
        }
    def create_meeting(self):
        view = self.env.ref('calendar.view_calendar_event_form')
        return {
            'name': _('Meeting'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'calendar.event',
            'type': 'ir.actions.act_window',
            'context': {'default_opportunity_id':self.id},
            'target': 'current'
        }
class helpdesk(models.Model):
    _inherit ='helpdesk.ticket'
    count_meeting = fields.Integer("count Meeting")

    def action_view_meeting(self):
        return {
            'name': _('Meeting'),
            'view_mode': 'form',
            'res_model': 'calendar.event',
            'type': 'ir.actions.act_window',
            'domain': [("ticket_id","=",self.id)],
            'target': 'current'
        }

    def create_meeting(self):
        view = self.env.ref('calendar.view_calendar_event_form')
        return {
            'name': _('Meeting'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'calendar.event',
            'type': 'ir.actions.act_window',
            'context': {'default_ticket_id':self.id},
            'target': 'current'
        }