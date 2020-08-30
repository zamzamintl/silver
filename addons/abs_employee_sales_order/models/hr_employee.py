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

from odoo import api,fields,models,_

class Employee(models.Model):
    _inherit = "hr.employee"

    sale_order_count = fields.Integer(compute='_get_count_list')

    # For treeview of sales order
    def get_sale_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Order',
            'view_mode': 'tree',
            'res_model': 'sale.order',
            'domain': [('user_id.employee_ids', '=', self.id),('date_order','!=',False)],
        }

    # For count sales order
    def _get_count_list(self):
        self.sale_order_count = self.env['sale.order'].search_count([('user_id.employee_ids', '=', self.id),('date_order','!=',False)])
