from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
class deliver(models.Model):
    _inherit='delivery.carrier'
    area=fields.Many2many('state.region1','delivery_carrier_area_rel', 'carrier_id', 'area_id',string='Area')
    """@api.constrains("area")
    def get_duplicate(self):
        for record in self.search([]):
            for rec in record.area:
                if rec in self.area and record.id != self.id:
                    raise ValidationError("Shipping Cost of area must be unique "+ rec.name)"""

    def _match_address(self, partner):
        self.ensure_one()
        if self.country_ids and (partner.country_id not in self.country_ids and partner.region_id not in self.area):
            return False
        if self.state_ids and (partner.state_id not in self.state_ids and partner.region_id not in self.area):
            return False
        if self.zip_from and (partner.zip or '').upper() < self.zip_from.upper():
            return False
        if self.zip_to and (partner.zip or '').upper() > self.zip_to.upper():
            return False
        if self.area:
           return True
