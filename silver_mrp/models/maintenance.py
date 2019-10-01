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


class MaintenanceEquipmentPartCategory(models.Model):
    _name = 'maintenance.equipment.part.category'

    name = fields.Char(string="name", required=False, )


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    part_categ_id = fields.Many2one('maintenance.equipment.part.category',
                                    string='Spare part Category')
