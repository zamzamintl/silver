from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
import logging
_logger = logging.getLogger(__name__)
class attac(models.Model):
    _inherit='ir.attachment'
    datas_fname=fields.Char("datas_fname")
