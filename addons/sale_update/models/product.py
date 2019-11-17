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

from datetime import datetime, timedelta

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
import logging

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools import pycompat

class ProductTag(models.Model):
    _name='product.tag'


    name=fields.Char(string='Name')

class ProductTemplate(models.Model):
    _inherit = "product.template"

    height=fields.Float('Height')
    width=fields.Float('Width')
    lenght=fields.Float('Lenght')

    product_tag_ids=fields.Many2many(comodel_name='product.tag',string='Product Tags')



class ProductProduct(models.Model):
    _inherit = "product.product"

    product_tag_ids=fields.Many2many(comodel_name='product.tag',string='Product Tags')


