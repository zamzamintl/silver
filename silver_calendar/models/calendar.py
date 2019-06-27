# -*- coding: utf-8 -*-

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

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError


class CalendarEventTime(models.Model):
    _name = "calendar.event.time"

    time=fields.Float('Time')
    note=fields.Char('Notes')

    event_id=fields.Many2one(comodel_name='calendar.event',string='Meeting')


class CalendarEvent(models.Model):
    _inherit = "calendar.event"


    calendar_time_ids=fields.One2many(comodel_name='calendar.event.time',string='Minutes',inverse_name='event_id')