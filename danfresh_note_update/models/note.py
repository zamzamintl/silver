# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2018-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Note(models.Model):
    _inherit = 'note.note'

    name = fields.Char('Title')
    task_id = fields.Many2one('project.task','Task')

    def action_create_task(self):
        self.ensure_one()
        task_obj = self.env['project.task']

        task_values = {
                'user_id': self.env.user.id,
                'name': self.name,
                'description': self.memo
            }
        task_id=task_obj.create(task_values)
        self.write({'task_id':task_id.id})
        return {
                'type': 'ir.actions.act_window',
                'res_model': 'project.task',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': task_id.id,
                'views': [(False, 'form')],
            }



    def action_view_task(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.task_id.id,
            'views': [(False, 'form')],
        }


