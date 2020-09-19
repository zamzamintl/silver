
from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit="project.task"


    task_sale_order_id = fields.Many2one('sale.order', string='Sale Order',readonly=True, help='This field displays Sales Order')
    count_order= fields.Integer("Count_order",compute="_get_orders")
    count_lead= fields.Integer("Count Tasks")
    count_ticket= fields.Integer("Count Tickets")
    # This function is used to check customer is selected or not if customer is selected than create a wizard
    @api.depends("task_sale_order_id")
    def _get_orders(self):
        for rec in self.search([]):
            orders=self.env['sale.order'].search([('source_project_task_id','=',rec.id)])
            if rec.task_sale_order_id:
                 rec.count_order=len(orders)
            else:
                rec.count_order=0
    def create_warning(self,context=None):
        for recrod in self:
            store_partner_id_task = self.partner_id.id
            if store_partner_id_task:
                return {
                        'name': ('Create Quotation'),
                        'view_type': 'form',
                        'view_mode': 'form',
                        'res_model': 'task.create.quotation',
                        'view_id': False,
                        'type': 'ir.actions.act_window',
                        'target':'new'
                       }
            else:
                raise ValidationError(_('Please Select Customer'))


    def action_view_sale_order(self):
        return {
            'name': ('orders'),
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',

            'domain': [('source_project_task_id', '=', self.id)],
            'target': 'current'
        }

    def create_lead(self):
        view = self.env.ref('crm.crm_lead_view_form')

        return {
            'name': _('Lead'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'context': {'default_task_id': self.id,},
            'target': 'current'
        }
    def create_ticket(self):
        view = self.env.ref('helpdesk.helpdesk_ticket_view_form')

        return {
            'name': _('Lead'),
            'view_mode': 'form',
            'view_id': view.id,
            'res_model': 'helpdesk.ticket',
            'type': 'ir.actions.act_window',
            'context': {'default_task_id': self.id,},
            'target': 'current'
        }
    def action_view_leads(self):
        view = self.env.ref('crm.crm_case_tree_view_leads')
        view_form = self.env.ref('crm.crm_lead_view_form')
        orders = self.env['crm.lead'].search([('task_id', '=', self.id)])
        ids = []
        for rec in orders:
            ids.append(rec.id)
        return {
            'name': _('leads'),
            'view_mode': 'tree,form',
            'view_type': 'form',
            'views': [(view.id, 'tree'), (view_form.id, 'form')],
            'res_model': 'crm.lead',
            'domain': [('id', 'in', ids)],
            'type': 'ir.actions.act_window',
            'target': 'current'
        }
    def action_view_ticket(self):
        view = self.env.ref('helpdesk.helpdesk_tickets_view_tree')
        view_form=self.env.ref('helpdesk.helpdesk_ticket_view_form')
        orders=self.env['helpdesk.ticket'].search([('task_id','=',self.id)])
        ids=[]
        for rec in orders:
            ids.append(rec.id)
        return {
            'name': _('Tickets'),
            'view_mode': 'tree,form',
            'view_type':'form',
            'views': [(view.id,'tree'),(view_form.id,'form')],
            'res_model': 'helpdesk.ticket',
            'domain':[('id','in',ids)],
            'type': 'ir.actions.act_window',
            'target':'current'
        }