# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
class Project(models.Model):
    _inherit = "project.project"

    owner_id = fields.Many2one('res.partner',string='Project Owner')
    consultant_id = fields.Many2one('res.partner',string='Consultant')
    construction_id = fields.Many2one('res.partner',string='Construction')
    system_integrator_id = fields.Many2one('res.partner',string='System integrator')
    image_ids = fields.One2many(comodel_name="project.image", inverse_name="project_id", string="Image Lines",
                                required=False, )