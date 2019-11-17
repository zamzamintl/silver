# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class AccountMove(models.Model):
    _inherit = ['account.move']

    draft_number = fields.Char(string='Draft Number')
