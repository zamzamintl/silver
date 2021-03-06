import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime

class product_template(models.Model):
    _inherit="product.template"
    installation=fields.Boolean("Installation",default=False)
class product_product(models.Model):
    _inherit="product.product"
    installation=fields.Boolean(related="product_tmpl_id.installation",default=False)