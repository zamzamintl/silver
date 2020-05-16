# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = []
        if not (name == '' and operator == 'ilike'):
            args += ['|', ('name', operator, name), ('phone', operator, name)]
        print(args)
        return super(ResPartner, self)._name_search(name='', args=args, operator='ilike', limit=limit,
                                                    name_get_uid=name_get_uid)
