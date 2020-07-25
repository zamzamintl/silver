import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime

class warehouse(models.Model):
    _name = "calenar.agenda"
    name=fields.Char("Name",required="1")
    code=fields.Char("Code",required="1")
    calendar=fields.Many2one("calendar.event")
class mintues(models.Model):
    _name = "mintues.meeting"
    name=fields.Char("Description")
    calendar=fields.Many2one("calendar.event")
    agenda=fields.Many2one("calenar.agenda",string="Agenda")
    code_agenda=fields.Char(related="agenda.code",string="Code")
    responisble=fields.Char("responisble")
    action_by=fields.Many2one("res.partner",string="Action By")
    @api.onchange("agenda")
    def get_agenda(self):
        
        return {'domain':{'agenda':[('id','in',self.calendar.agenda.ids)]}}
    @api.onchange("action_by")
    def get_changes(self):
        
        return {'domain':{'action_by':[('id','in',self.calendar.partner_ids.ids)]}}
    
