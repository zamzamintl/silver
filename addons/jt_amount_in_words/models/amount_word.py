from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from num2words import num2words

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    # @api.multi
    @api.constrains("amount_total","num_word_ar")
    def _compute_amount_in_word(self):
        for rec in self:
            if rec.amount_total:
                rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
                rec.num_word_ar=num2words(round(rec.amount_total,2), lang='ar')

    num_word = fields.Char(string="Amount In Words:", compute='_compute_amount_in_word')
    num_word_ar = fields.Char(string="Amount In Word ar", compute='_compute_amount_in_word')


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    # @api.multi
    @api.constrains("amount_total","num_word_ar")
    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word_ar=num2words(round(rec.amount_total,2), lang='ar')

    num_word = fields.Char(string="Amount In Words:", compute='_compute_amount_in_word')
    num_word_ar = fields.Char(string="Amount In Word ar", compute='_compute_amount_in_word')


class InvoiceOrder(models.Model):

    _inherit = 'account.move'

    # @api.multi
    @api.constrains("amount_total","num_word_ar")
    def _compute_amount_in_word(self):
        for rec in self:
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word_ar=num2words(round(rec.amount_total,2), lang='ar')

    num_word = fields.Char(string="Amount In Words:", compute='_compute_amount_in_word')
    num_word_ar = fields.Char(string="Amount In Word ar", compute='_compute_amount_in_word')
