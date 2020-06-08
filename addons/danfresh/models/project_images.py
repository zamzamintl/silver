# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta

class ProjectImages(models.Model):
    _name = 'project.image'
    _rec_name = 'name'
    _description = 'Project Images'

    name = fields.Char("Description", required=True)
    image = fields.Binary(string="Image", required=False)
    file_name = fields.Char("File Name")
    project_id = fields.Many2one(comodel_name="project.project", string="Project", required=False, )

