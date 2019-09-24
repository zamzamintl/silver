# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError


class ReportInvoiceSum(models.AbstractModel):
    _name = 'report.silver_account.report_invoice_sum'

    def get_lines(self, invoice):
        if not invoice:
            return []

        lines = []
        products = invoice.mapped('invoice_line_ids.product_id')
        for product in products:
            pr_lines = invoice.invoice_line_ids.filtered(
                lambda l: l.product_id.id == product.id)
            discount_lines = pr_lines.mapped('discount')
            if len(discount_lines) <= 1:
                qty = sum([l.quantity for l in pr_lines])
                total = sum([l.price_total for l in pr_lines])
                subtotal = sum([l.price_subtotal for l in pr_lines])
                pr_data = {
                    'name': product.name,
                    'uom': product.uom_id.name,
                    'qty': qty,
                    'discount': discount_lines[0] if discount_lines else 0,
                    'subtotal': subtotal,
                    'total': total,
                    'tax_ids': pr_lines.mapped('invoice_line_tax_ids'),
                    'price': sum(pr_lines.mapped('price_unit'))/len(pr_lines.mapped('price_unit')) or 0,
                }
                lines.append(pr_data)
            else:
                for d_line in discount_lines:
                    pr_d_lines = invoice.invoice_line_ids.filtered(lambda
                                                                       l: l.product_id.id == product.id and l.discount == d_line)
                    qty = sum([l.quantity for l in pr_d_lines])
                    subtotal = sum([l.price_subtotal for l in pr_d_lines])
                    total = sum([l.price_total for l in pr_d_lines])
                    pr_data = {
                        'name': product.name,
                        'uom': product.uom_id.name,
                        'qty': qty,
                        'discount': discount_lines[0] if discount_lines else 0,
                        'subtotal': subtotal,
                        'tax_ids': pr_d_lines.mapped('invoice_line_tax_ids'),
                        'total': total,
                        'price':sum(pr_d_lines.mapped('price_unit'))/len(pr_d_lines.mapped('price_unit')) or 0,
                    }
                    lines.append(pr_data)
        return lines

    @api.model
    def _get_report_values(self, docids, data=None):
        invoice_ids = self.env['account.invoice'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': invoice_ids,
            'data': data,
            'get_lines': self.get_lines
        }
