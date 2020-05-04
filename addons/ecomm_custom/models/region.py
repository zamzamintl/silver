from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
class sregion(models.Model):
    _name="state.region1"
    state_id=fields.Many2one('res.country.state',string="City")
    region2=fields.One2many('state.region2','region1',string='District')
    name=fields.Char("Area")
class state(models.Model):
    _inherit='res.country.state'
    region=fields.One2many('state.region1','state_id',string='area')
class region2(models.Model):
    _name='state.region2'
    name=fields.Char("District")
    region1=fields.Many2one('state.region1',string='Area')
    region3=fields.One2many('state.region','region2',string='Partition')
class region3(models.Model):
    _name='state.region'
     
    name=fields.Char("Partition")
    
    region2=fields.Many2one('state.region2',string='District')
    
