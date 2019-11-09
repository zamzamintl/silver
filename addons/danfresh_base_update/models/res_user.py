# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class Users(models.Model):
    _inherit = "res.users"

    is_kanban_read = fields.Boolean('Tasks Kanban UnDragable', default=False)

    @api.constrains('groups_id')
    def _check_one_user_type(self):
        res = super(Users, self)._check_one_user_type()
        return res
