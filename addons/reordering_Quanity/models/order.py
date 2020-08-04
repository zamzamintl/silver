import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from collections import OrderedDict
from datetime import datetime
 
     
class order(models.Model):
    _inherit="sale.order.line"
    @api.onchange("state")
    def get_stata_of_quantity(self):
        if self.state !='draft':
