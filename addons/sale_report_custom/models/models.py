import logging
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError
from odoo.http import request
class sales_repor(models.Model):
    _inherit = 'sale.report'
    customer_order_delivery_date = fields.Date("Delivery Date")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['customer_order_delivery_date'] = ", s.customer_order_delivery_date AS customer_order_delivery_date"
        groupby+=',s.customer_order_delivery_date'
        return super(sales_repor, self)._query(with_clause, fields, groupby, from_clause)