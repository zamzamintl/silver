# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class SaleQuotation(models.Model):
    _inherit = 'sale.order'

    name = fields.Char(track_visibility='onchange')
    client_order_ref = fields.Char(track_visibility='onchange')
    date_order = fields.Datetime(track_visibility='onchange')
    user_id = fields.Many2one(track_visibility='onchange')
    partner_id = fields.Many2one(track_visibility='onchange')
    partner_invoice_id = fields.Many2one(track_visibility='onchange')
    partner_shipping_id = fields.Many2one(track_visibility='onchange')
    analytic_account_id = fields.Many2one(track_visibility='onchange')
    note = fields.Text(track_visibility='onchange')
    amount_total = fields.Monetary(track_visibility='onchange')

