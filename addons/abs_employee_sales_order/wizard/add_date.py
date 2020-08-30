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

from odoo import fields,api,models,_
from odoo.exceptions import ValidationError

class AddDate(models.TransientModel):
    _name = 'add.date'
    _description = 'Add Date'

    start_date = fields.Date('Start date',required=True)
    end_date = fields.Date("End Date",required=True)

    def print_date(self):
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        
        data = {}
        data['start_date'] = self.start_date
        data['end_date'] =  self.end_date
        return self._print_report(data)

    def _print_report(self,data):
        return self.env.ref('abs_employee_sales_order.action_sale_order_report').report_action(self, data=data)

    @api.constrains('start_date','end_date')
    def constrains_date(self):
        if self.start_date and self.end_date:
            if not self.start_date <= self.end_date:
                raise ValidationError("Please enter the valid Date. End Date should be greater than Start Date.")




