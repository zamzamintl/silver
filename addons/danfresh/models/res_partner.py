# -*- coding: utf-8 -*-

from odoo import models, fields, api
class partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('uniq_ref','UNIQUE(ref)','Internal Reference Is Unique Per Partner!!')
    ]