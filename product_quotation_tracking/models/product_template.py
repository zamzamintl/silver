# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # TODO Override Default Field for Tracking Porpoise
    name = fields.Char('Name', track_visibility='onchange')
    type = fields.Selection(track_visibility='onchange')
    categ_id = fields.Many2one(track_visibility='onchange')
    list_price = fields.Float(track_visibility='onchange')
    standard_price = fields.Float(track_visibility='onchange')
    sale_ok = fields.Boolean(track_visibility='onchange')
    purchase_ok = fields.Boolean(track_visibility='onchange')
    uom_id = fields.Many2one(track_visibility='onchange')
    default_code = fields.Char(track_visibility='onchange')
    barcode = fields.Char(track_visibility='onchange')
    invoice_policy = fields.Selection(track_visibility='onchange')
    purchase_method = fields.Selection(track_visibility='onchange')
    sale_delay = fields.Float(track_visibility='onchange')
