import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request

class order(models.Model):
    _inherit='sale.order'
    phone_cst=fields.Char(related='partner_id.phone',string='Phone')
    @api.constrains("customer_order_delivery_date","order_line")
    def get_changes_order_line(self):
        _logger.info("DELIVER DATE")
        _logger.info(self.env.uid)
        if self.create_uid.id !=self.env.uid:
            _logger.info("change date")
            partner_id=self.env["res.users"].search([('id','=',self.env.uid)]).partner_id
            if self.customer_order_delivery_date:
                value={
                'body':"Change Delivery Date by "+ partner_id.name,
                'res_id':self.id,
                'model':'sale.order',
                'message_type':'notification',
                  }
                self.message_ids.create(value)
            if self.order_line:
                value={
                'body':"Change list of products by "+ partner_id.name,
                'res_id':self.id,
                'model':'sale.order',
                'message_type':'notification',
                  }
                self.message_ids.create(value)
