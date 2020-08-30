# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2020-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api, models, fields
from odoo.exceptions import Warning
import datetime

class SaleOrderReport(models.AbstractModel):
    _name="report.abs_employee_sales_order.sale_order_report"
    _description = 'Sale Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        employee_id = self.env[self.model].browse(self.env.context.get('active_id')) # to get current employee
        
        order_list = [] # to store sales order
        order_ids = self.env['sale.order'].search([('user_id.employee_ids', '=', employee_id.id)])
        for order in order_ids:
            lst = str(order.date_order).split('.') # To get only datetime
            conf_date = datetime.datetime.strptime(str(lst[0]), '%Y-%m-%d %H:%M:%S').date() # To get only date

            # To get orderlist between start date and end date
            if str(conf_date) >= data['start_date'] and str(conf_date) <= data['end_date']:
                order_list.append(order)
        
        # if sales order are found it return all detail which is required in report, else it return warning
        if len(order_list) > 0:
            docargs = {
                    'employee_id': employee_id,
                    'start_date': self.get_date(data['start_date']),
                    'end_date': self.get_date(data['end_date']),
                    'order_list': order_list,
                  }
            if docargs:
                return docargs
        else:
            raise Warning('Sales Order not found !!!')

    # To get date in month/day/year format
    def get_date(self,date):
        return datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%m/%d/%Y')

