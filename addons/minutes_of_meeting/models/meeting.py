import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime

 
class order(models.Model):
    _inherit="calendar.event"
    agenda=fields.Many2many("calenar.agenda","agenda_id","id",string="Agenda")
    minute_meeting=fields.One2many("mintues.meeting","calendar",string="minutes of meeting")
    presented_by=fields.Many2one("res.users" ,string="Presented By")

    ticket_id = fields.Many2one("helpdesk.ticket",string="Ticket")


    @api.constrains("ticket_id")
    def get_ticket_id(self):
        self.ticket_id.count_meeting += 1