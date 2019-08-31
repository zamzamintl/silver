# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
class OpportunityTypes(models.Model):
    _name = "opportunity.type"

    name = fields.Char('Name')
    code = fields.Char('Code')
    line_ids = fields.One2many('opportunity.type.line','opportunity_type_id',string="Lines")

class OpportunityTypes_lines(models.Model):
    _name = "opportunity.type.line"

    name = fields.Char('Name')
    code = fields.Char('Code')
    opportunity_type_id = fields.Many2one('opportunity.type',string='Opportunity Type')

