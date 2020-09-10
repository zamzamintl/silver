from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)
class sale_order(models.Model):
    _inherit = 'sale.order'
    count_task= fields.Integer("Tasks")
    count_ticket= fields.Integer("Tickets")


    def action_view_task(self):
        return {
            'name': _('Task'),
            'view_mode': 'tree,form',
            'res_model': 'project.task',
            'type': 'ir.actions.act_window',
            'domain': [('task_sale_order_id','=', self.id)],
            'target': 'current'
        }
    def create_task(self):
        view = self.env.ref('project.view_task_form2')
        return {
            'name': _('Task'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'project.task',
            'type': 'ir.actions.act_window',
            'context': {'default_task_sale_order_id': self.id,},
            'target': 'current'
        }
    def action_view_ticket(self):
        return {
            'name': _('Tickets'),
            'view_mode': 'tree,form',
            'res_model': 'helpdesk.ticket',
            'type': 'ir.actions.act_window',
            'domain': [('sale_order_id','=', self.id)],
            'target': 'current'
        }
    def create_ticket(self):
        view = self.env.ref('helpdesk.helpdesk_ticket_view_form')
        return {
            'name': _('Tickets'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'helpdesk.ticket',
            'type': 'ir.actions.act_window',
            'context': {'default_sale_order_id': self.id,},
            'target': 'current'
        }
class task(models.Model):
    _inherit='project.task'
    @api.constrains("task_sale_order_id")
    def get_sale_order_count(self):
        if self.task_sale_order_id:
           self.task_sale_order_id.count_task+=1