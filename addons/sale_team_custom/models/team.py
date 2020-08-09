import logging
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError
from odoo.http import request

class salesteam(models.Model):
    _inherit = 'crm.team'
    @api.constrains("member_ids","user_id")
    def get_members(self):
        for team in self:
            team.favorite_user_ids = [(4, member.id) for member in team.member_ids]
            team.user_id.members = [(4, member.id) for member in team.member_ids]
        users = self.env["res.users"].search([])
        for rec in self.user_id.members:
            if rec.sale_team_id.user_id.id != self.user_id.id:
                self.user_id.members=[(3,rec.id)]







class users(models.Model):
    _inherit = 'res.users'
    members = fields.Many2many("res.users","member","id",string="Memebers")

