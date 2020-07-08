import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request

class activity(models.Model):
    _inherit='helpdesk.ticket'
    @api.constrains("lead_id")
    def get_activity(self):
        _logger.info("RRRRRRRRRRRRRRRRRRRR")
        model=self.env['ir.model'].search([('model','=','crm.lead')])
        act=self.env['mail.activity.type'].search([('name','=','create by Ticket')])
        if self.lead_id:
            
            self.lead_id.activity_ids.create({'res_id':self.lead_id.id,'activity_type_id':act.id,'res_model_id':model.id})



