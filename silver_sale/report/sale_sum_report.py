# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError


class ReportInvoiceSum(models.AbstractModel):
    _name = 'report.silver_sale.report_sale_sum'

    def get_lines(self, docids):
        sale_ids = self.env['sale.order'].browse(docids)
        lines = []
        for sale in sale_ids:
            if not sale.employee_id:
                raise UserError(_('Sale Order : %s Has no sale Rep'%sale.name))
        employee_ids=sale_ids.mapped('employee_id')
        emp_data = {}
        for emp in employee_ids:
            emp_data[emp]=[]
            emp_sale_ids=sale_ids.filtered(lambda s:s.employee_id.id == emp.id)
            products = sale_ids.mapped('order_line.product_id')
            for product in products:
                pr_lines = emp_sale_ids.mapped('order_line').filtered(
                    lambda l: l.product_id.id == product.id)
                qty = sum([l.product_uom_qty for l in pr_lines])
                pr_data = {
                    'name': product.display_name,
                    'uom': product.uom_id.name,
                    'qty': qty,
                }
                emp_data[emp].append(pr_data)

        return emp_data

    @api.model
    def _get_report_values(self, docids, data=None):
        sale_ids = self.env['sale.order'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'data': data,
            'employee_lines': self.get_lines(docids)
        }
