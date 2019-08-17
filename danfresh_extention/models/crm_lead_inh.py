# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
class CrmLead(models.Model):
    _inherit = 'crm.lead'


    opportunity_id = fields.Many2one('opportunity.type',string='Opportunity')
    name = fields.Char('Opportunity',default='New', required=False, index=True)
    opportunity_type_line_id = fields.Many2one('opportunity.type.line',string='Opportunity Line')
    note = fields.Char('Notes')
    op_type = fields.Selection(string="OP Type", selection=[('none', 'None'), ('project', 'Project'),('enduser', 'End User'), ], required=True, default='none')
    @api.onchange('opportunity_id')
    def onchange_field_name(self):
        for rec in self:
            if rec.opportunity_id:
                return {'domain': {'opportunity_type_line_id': [('id','in',rec.opportunity_id.line_ids.ids)]}}
            else:
                return {'domain': {'opportunity_type_line_id': [('id','=',False)]}}

    consultant_id = fields.Many2one('res.partner',string='Consultant')
    innterior_design_id = fields.Many2one('res.partner',string='Innterior Design')
    developer_id = fields.Many2one('res.partner',string='Developer')
    construction_id = fields.Many2one('res.partner',string='Construction')
    electromechanical_id = fields.Many2one('res.partner',string='Electromechanical')
    system_integrator_id = fields.Many2one('res.partner',string='System_integrator')
    project_manager_id = fields.Many2one('res.partner',string='Project_manager')
    owner_id = fields.Many2one('res.partner',string='Owners')
    other_id = fields.Many2one('res.partner',string='Others')