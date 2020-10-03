
from odoo import api, models
from dateutil.relativedelta import relativedelta
import datetime
import logging
import pytz
from collections import OrderedDict
_logger = logging.getLogger(__name__)


class ReportProductSale(models.AbstractModel):
    _name = "report.sale_report_xlx.sale_report_xlx"
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, lines):
        report_name='SO'
        sheet = workbook.add_worksheet(report_name[:31])
        bold = workbook.add_format({'bold': True})
        unbold = workbook.add_format({'bold': False})
        date_from = data["form"]["date_from"]
        date_to = data["form"]["date_to"]
        customer = data["form"]["customer"]
        domain=[]
        if date_from:
            domain.append(('customer_order_delivery_date','>=',date_from))
        if date_to:
            domain.append(('customer_order_delivery_date', '>=', date_to))
        if customer:
            report_name= self.env['res.partner'].search([('id','=',customer)]).name
            ids=[]
            ids.append(customer)
            partner_ids = self.env['res.partner'].search([('parent_id','=',customer)])
            for rec in partner_ids:
                ids.append(rec.id)
            domain.append(('partner_id', 'in', ids))
        sheet.write(1, 2, 'Customer', bold)
        sheet.write(1, 3, 'Store', bold)

        sheet.write(1, 4, 'Date', bold)
        sheet.write(1, 5, 'So', bold)
        sheet.write(1, 6, 'Item', bold)
        sheet.write(1, 7, 'Q', bold)
        sheet.write(1, 8, 'Price', bold)
        sheet.write(1, 9, 'Value', bold)
        sheet.write(1, 10, 'Amount After Vat', bold)
        row = 1
        col = 2
        sale_order = self.env['sale.order'].search(domain,order='customer_order_delivery_date asc')
        for record in sale_order:
            row+=1
            col = 2

            for rec in record.order_line:

                col+=1

                if record.partner_id.region_id:
                    sheet.write(row, 3, record.partner_id.region_id.name, unbold)
                else:
                    sheet.write(row, 3 , '', unbold)

                if col == 3:
                   sheet.write(row, 2, record.partner_id.name, unbold)
                   if record.customer_order_delivery_date:
                        sheet.write(row, 4, record.customer_order_delivery_date, unbold)
                   else:
                       sheet.write(row, 4, '', unbold)

                   sheet.write(row, 5, record.name, unbold)
                else:
                    sheet.write(row, 2, '', unbold)
                    sheet.write(row, 4 , '', unbold)
                    sheet.write(row, 5 , '', unbold)

                sheet.write(row, 6, rec.product_id.name, unbold)
                sheet.write(row, 7, rec.product_uom_qty, unbold)
                sheet.write(row, 8, rec.price_unit, unbold)
                sheet.write(row, 9, rec.price_subtotal, unbold)
                sheet.write(row, 10, rec.price_total, unbold)






    # def _get_report_values(self, docids, data=None):
    #     date_from = data["form"]["date_from"]
    #     date_to = data["form"]["date_to"]
    #     customer = data["form"]["customer"]
    # 
    #     total_sale = 0.0
    #     period_value = ""
    #     domain = [("type", "=", "out_invoice")]
    #     if date_from:
    #         domain.append(("invoice_date", ">=", date_from))
    #     if date_to:
    #         domain.append(("invoice_date", "<=", date_to))
    #     if customer:
    #         domain.append(("partner_id", "in", customer))
    # 
    #     list = []
    #     customer_list = []
    #     invoice_ids = self.env["account.move"].search(domain, order="invoice_date asc")
    #     old_timezone = pytz.timezone("UTC")
    #     new_timezone = pytz.timezone("Africa/Cairo") 
    #     total_amount=0
    #     for inv in invoice_ids:
    #         if inv.partner_id and inv.type == 'out_invoice':
    #             if inv.partner_id not in customer_list:
    #                 customer_list.append(inv.partner_id) 
    #             total_amount+=inv.amount_total
    #             list.append(
    #                 {
    #                     "so_number": inv.name,
    #                      
    #                     "invoice_number": inv.name,
    #                     "inv_name": inv.name,
    #                     "date_in": inv.invoice_date,
    #                     "partner": inv.partner_id.name,
    #                     "total": inv.amount_total,
    #                     
    #                      
    #                    
    #                 }
    #             )
    #     _logger.info("CUUSTOMER STATMENT")
    #     
    #     _logger.info(invoice_ids)
    #     _logger.info(customer_list)
    #     
    #     return {
    #             "doc_ids": data["ids"],
    #             "doc_model": data["model"],
    #             "period": period_value,
    #             "date_from": date_from,
    #             "date_to": date_to,
    #             "sale_orders": invoice_ids,
    #             "data_check": False,
    #             "total_amount":total_amount,
    #             "customer_list":customer_list,
    #             "name_report":'كشــف حســـاب عميل'
    #         }

