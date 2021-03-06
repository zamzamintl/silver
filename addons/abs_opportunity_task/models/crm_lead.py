# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Ascetic Business Solution <www.asceticbs.com>
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
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = "crm.lead"

    task_count = fields.Integer(compute='_compute_task_count', string="Tasks Count")
 
    def _compute_task_count(self):
        _logger.info("_compute_task_count")
        count = 0
        task_ids = self.env['project.task'].search([])
        for record in self:
            count=0
            if record:
                for task_id in task_ids:
                    if record.partner_id == task_id.partner_id:
                        count=count+1 
            record.task_count = count
        
