# -*- coding: utf-8 -*-

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

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError




class Project(models.Model):
    _inherit = "project.project"


    task_progress=fields.Float('Tasks Progress',compute='compute_task_progress')




    def compute_task_progress(self):
        for proj in self:
            tot_tasks=len(proj.task_ids)
            done_tasks=len([tsk for tsk in proj.task_ids if tsk.kanban_state == 'done'])
            proj.task_progress= done_tasks*100/tot_tasks if tot_tasks>0 else 0