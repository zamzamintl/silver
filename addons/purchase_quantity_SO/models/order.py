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
    _inherit="sale.order"
  
    def action_purchase_order(self):
        _logger.info(self.env.ref('warehouse_at_salesorder.po_so_form2').id)
        lines=[]
        for rec in self:
            lines.append(rec.id)
        _logger.info("888888")
        _logger.info(lines)
        return{ 'name':'Warehouse',
            'res_model': 'warehouse.sales',
            'target': 'new',
             'view_type': 'form',
             'view_mode': 'form',
            'view_id':self.env.ref('warehouse_at_salesorder.po_so_form2').id ,
            'context':{'default_sales_order':lines},
            'type': 'ir.actions.act_window', }
        
     
   

