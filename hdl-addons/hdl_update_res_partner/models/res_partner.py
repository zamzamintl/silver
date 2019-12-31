# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HdlUpdatePartner(models.Model):
    _inherit = 'res.partner'

    partner_category_id = fields.Many2one('res.partner.category.partner',string='Category')


class HdlResCaregory(models.Model):
    _name = 'res.partner.category.partner'

    name = fields.Char(string='Name')
    parent_id = fields.Many2one('res.partner.category.partner',string='Parent Category')
    active = fields.Boolean('Active', default=True)