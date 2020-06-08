# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions,_

class Employee(models.Model):
    _inherit = "hr.employee"

    def action_open_tasks(self):

        user_id = self.user_id
        return {
            'name': (_('Tasks')),
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('user_id', '=', self.user_id.id),('user_id', '!=', False)],
            'target': 'current',
        }
