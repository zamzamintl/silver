# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_
from odoo.exceptions import ValidationError




class Project(models.Model):
    _inherit = "project.project"

    department_id = fields.Many2one('hr.department',string="Department")

