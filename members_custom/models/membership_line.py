# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
from dateutil.relativedelta import relativedelta
import math


class MembershipLine(models.Model):
    _inherit = 'membership.membership_line'

    is_paused = fields.Boolean(string="Paused", default=False)
    is_resumed = fields.Boolean(string="Resumed", default=True)

    pause_date = fields.Date(string="Pause Date", required=False, )
    resume_date = fields.Date(string="Resume Date", required=False, )

    def action_pause(self):
        self.is_paused = True
        self.is_resumed = False
        self.pause_date = date.today()
        self.resume_date = False

    def action_resume(self):
        self.is_resumed = True
        self.is_paused = False
        self.resume_date = date.today()
        if self.resume_date and self.pause_date:
            year, month, day = self.calc_difference(self.resume_date, self.pause_date)
            if year > 0:
                self.date_to += relativedelta(years=year)
            if month > 0:
                self.date_to += relativedelta(months=month)
            if day > 0:
                self.date_to += relativedelta(days=day)

    def calc_difference(self, start, stop):
        difference = start - stop
        year = difference.days // (365)
        month = (difference.days - year * 365) // (365 / 12)
        day = ((difference.days - year * 365) - month * (365 / 12))
        return year, month, day

    @api.model
    def create(self, vals):
        membership_line = super(MembershipLine, self).create(vals)
        membership_id = membership_line.membership_id
        membership_type = membership_id.member_type
        start_date = self.env.context.get('start_date')
        if start_date:
            if membership_type == 'duration':
                duration = membership_id.duration
                if duration == 'monthly':
                    membership_line.write({
                        'date': start_date,
                        'date_from': start_date,
                        'date_to': start_date + relativedelta(months=1),
                    })
                elif duration == 'quarterly':
                    membership_line.write({
                        'date': start_date,
                        'date_from': start_date,
                        'date_to': start_date + relativedelta(months=3),
                    })
                elif duration == 'half_year':
                    membership_line.write({
                        'date': start_date,
                        'date_from': start_date,
                        'date_to': start_date + relativedelta(months=6),
                    })
                elif duration == 'yearly':
                    membership_line.write({
                        'date': start_date,
                        'date_from': start_date,
                        'date_to': start_date + relativedelta(months=12),
                    })

        print(membership_line.date_from)
        print(membership_line.date_to)
        return membership_line

    @api.multi
    def name_get(self):
        new_format = []
        for rec in self:
            new_info = "{}( {}-{} )".format(rec.membership_id.name, rec.date_from, rec.date_to)
            new_format.append((rec.id, new_info))
        return new_format

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args if args else []
        if not (name == '' and operator == 'ilike'):
            args += ['|', '|',
                     ('membership_id.name', operator, name),
                     ('date_from', operator, name),
                     ('date_to', operator, name)]
        return super(MembershipLine, self)._name_search(name='', args=args, operator='ilike', limit=limit,
                                                        name_get_uid=name_get_uid)
