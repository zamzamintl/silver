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


class DocumentFolder(models.Model):
    _inherit = 'documents.folder'


    published_projects = fields.Boolean(string="Published Projects",  )