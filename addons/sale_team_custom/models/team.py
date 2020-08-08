import logging
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError
from odoo.http import request
class salesteam(models.Model):
    _inherit = 'crm.teamsorder'
    count_memeber = fields.Integer(compute='_get_members')
    @api.depends("member_ids")
    def _get_members(self):
        for rec in self.member_ids:
            if self.user_id and rec.id not in self.user_id.members:
                self.user_id.members=[(4,rec.id)]
class users(models.Model):
    _inherit = 'res.users'
    members = fields.Many2many("res.users","member","id",string="Memebers")