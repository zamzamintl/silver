
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
from datetime import datetime





class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        activity_obj = self.env['mail.activity'].sudo()
        activty_type = self.env['mail.activity.type'].sudo().search(
            [('name', '=', 'To Do')], limit=1)
        if res.picking_type_id and res.picking_type_id.activity_user_ids:
            for usr in res.picking_type_id.activity_user_ids:
                new_activity = activity_obj.create({
                    'summary': 'Picking No : %s Has Been Created ,Please Check'%res.name,
                    'activity_type_id': activty_type.id,
                    'res_model_id': self.env['ir.model'].search(
                        [('model', '=', 'stock.picking')], limit=1).id,
                    'res_id': res.id,
                    'date_deadline': datetime.today(),
                    'user_id': usr.id
                })
        return res


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    activity_user_ids=fields.Many2many(comodel_name='res.users',string='Activity Users')



