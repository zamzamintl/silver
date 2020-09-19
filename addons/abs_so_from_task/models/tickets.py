
from odoo import api,fields,models,_
from odoo.exceptions import ValidationError
class ticket(models.Model):
    _inherit='helpdesk.ticket'

    task_id = fields.Many2one("project.task", string="Task")
    @api.constrains("task_id")
    def save_tasks(self):
        if self.task_id:
            self.task_id.count_ticket += 1