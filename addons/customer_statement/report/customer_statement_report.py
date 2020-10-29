
from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz
from collections import OrderedDict
_logger = logging.getLogger(__name__)


class ReportProductSale(models.AbstractModel):
    _name = "report.customer_statement.customer_statement_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        date_from = data["form"]["date_from"]
        date_to = data["form"]["date_to"]
        customer = data["form"]["customer"]
        check = data["form"]["check"]

        total_sale = 0.0
        period_value = ""
        domain = [("type", "=", "out_invoice")]
        if date_from:
            domain.append(("invoice_date", ">=", date_from))
        if date_to:
            domain.append(("invoice_date", "<=", date_to))
        if customer:
            domain.append(("partner_id", "in", customer))

        list = []
        customer_list = []
        invoice_ids = self.env["account.move"].search(domain, order="invoice_date asc")
        old_timezone = pytz.timezone("UTC")
        new_timezone = pytz.timezone("Africa/Cairo") 
        total_amount=0
        for inv in invoice_ids:
            if inv.partner_id and inv.type == 'out_invoice':
                if inv.partner_id not in customer_list:
                    customer_list.append(inv.partner_id) 
                total_amount+=inv.amount_total
                list.append(
                    {
                        "so_number": inv.name,
                         
                        "invoice_number": inv.name,
                        "inv_name": inv.name,
                        "date_in": inv.invoice_date,
                        "partner": inv.partner_id.name,
                        "total": inv.amount_total,
                        
                         
                       
                    }
                )

        
        return {
                "doc_ids": data["ids"],
                "doc_model": data["model"],
                "period": period_value,
                "date_from": date_from,
                "date_to": date_to,
                "sale_orders": invoice_ids,
                "data_check": False,
                "total_amount":total_amount,
                "customer_list":customer_list,
                "name_report":'كشــف حســـاب عميل'
            }

