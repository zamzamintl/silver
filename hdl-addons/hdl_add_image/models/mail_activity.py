from odoo import models, fields, api


class hdl_add_mail_activity(models.Model):
    _inherit = 'mail.activity'

    datetime_deadline = fields.Datetime('Due Date', index=True, required=True)