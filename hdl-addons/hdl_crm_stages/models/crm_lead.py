# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_
from odoo.exceptions import ValidationError




class hdl_crm_stages(models.Model):
    _inherit = "crm.stage"

    stage_fields_ids = fields.Many2many('ir.model.fields', string='Fields', domain=[('model','=','crm.lead')])





class hdl_crm_lead(models.Model):
    _inherit = "crm.lead"


    def write(self,vals):
        res = super(hdl_crm_lead, self).write(vals)
        if vals.get('stage_id'):
            stage_id = self.env["crm.stage"].browse(self.stage_id.id)
            fields=[f.name for f in  stage_id.stage_fields_ids]
            for lead  in self:
                for field in fields:
                    if not getattr(lead,field,False):
                        raise ValidationError(_('Please set the following filed first %s'%field))
        return res







class hdl_crm_stages_wizard(models.TransientModel):

    _inherit = 'crm.lead2opportunity.partner'


    def action_apply_one(self):
            lead = self.env['crm.lead'].browse(self._context['active_id'])
            for record in lead:
                if not record.mobile:
                    raise ValidationError(
                        _('The field mobile required.'))
                else :
                    self.action_apply()

