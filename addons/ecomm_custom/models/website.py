
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
import logging 
_logger = logging.getLogger(__name__)
class website_cust(http.Controller):
    def values_postprocess(self, order, mode, values, errors, error_msg):
        _logger.info("ffffffffffffffff")
        _logger.info("values_postprocess")
        new_values = {}
        authorized_fields = request.env['ir.model']._get('res.partner')._get_form_writable_fields()
         
        _logger.info(values)
        _logger.info(authorized_fields)
        for k, v in values.items():
            _logger.info("KKKKK")
            _logger.info(k)
            _logger.info(v)
            # don't drop empty value, it could be a field to reset
            if k=='mobile' or k=='floor'or k=='block':
                new_values[k] = v

            if k in authorized_fields and v is not None:
                new_values[k] = v
            else:  # DEBUG ONLY
                if k not in ('field_required', 'partner_id', 'callback', 'submitted'): # classic case
                    _logger.debug("website_sale postprocess: %s value has been dropped (empty or not writable)" % k)

        new_values['customer'] = True
        new_values['team_id'] = request.website.salesteam_id and request.website.salesteam_id.id
        new_values['user_id'] = request.website.salesperson_id and request.website.salesperson_id.id
        new_values['website_id'] = request.website.id

        lang = request.lang if request.lang in request.website.mapped('language_ids.code') else None
        if lang:
            new_values['lang'] = lang
        if mode == ('edit', 'billing') and order.partner_id.type == 'contact':
            new_values['type'] = 'other'
        if mode[1] == 'shipping':
            new_values['parent_id'] = order.partner_id.commercial_partner_id.id
            new_values['type'] = 'delivery'
        _logger.info("new value")
        _logger.info(new_values)
        return new_values, errors, error_msg

class partner((models.Model)):
    _inherit="res.partner"
    floor=fields.Char("Floor")
    block=fields.Char("Block")