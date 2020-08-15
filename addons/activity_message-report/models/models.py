from odoo import models, fields, api


class activity_message_report(models.Model):
     _name = 'activity.message.report'
     description =fields.Char("Description")
     res_model = fields.Char("Model")
     user_id = fields.Many2one("res.users","Assigned")
     due_date = fields.Date("Due date")
     res_id = fields.Char("res_id")
     author_id = fields.Many2one("res.partner","Author")
     type=fields.Char(string="Activity Type" ,default="Message")
     def action_open_record(self):
         return {
             'name':'Activity',
             'view_mode': 'tree,form',
             'view_type': 'form',
             'res_model': self.res_model,
             'domain': [('id', '=', self.res_id)],
             'type': 'ir.actions.act_window',
             'target': 'current'
         }
class IVITY(models.Model):
    _inherit ="mail.activity"
    created =fields.Boolean("Note",compute='_create_activity_record',store=True,default=False)
    @api.depends("date_deadline")
    def _create_activity_record(self):
        print("%%%%%%%%%%%%%%%%")
        activity=self.env["activity.message.report"]
        for rec  in self.search([]):
            if not rec.created:
                rec.created=True
                activity.create({'description':rec.res_name,'res_model':str(rec.res_model),'due_date':rec.date_deadline,
                'res_id':rec.res_id,'author_id':rec.create_uid.id,'type':rec.activity_type_id.name,
                                 'user_id':rec.user_id.partner_id.id})
class  notes(models.Model):
    _inherit ="mail.message"
    created =fields.Boolean("Note",compute='_create_activity_record',store=True,default=False)

    @api.depends("date")
    def _create_activity_record(self):
        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        activity=self.env["activity.message.report"]
        for rec  in self.search([]):
            if not rec.created:
                rec.created=True
                activity.create({'description':rec.description,'res_model':str(rec.model),'due_date':rec.date,
                'res_id':rec.res_id,'author_id':rec.author_id.id,})