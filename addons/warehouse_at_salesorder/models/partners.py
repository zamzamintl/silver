import logging
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError
from odoo.http import request
from collections import OrderedDict
from datetime import datetime
class partner(models.Model):
    _inherit = 'res.partner'
    default_purchase_oer = fields.Boolean(default=False,string="Default vendor")