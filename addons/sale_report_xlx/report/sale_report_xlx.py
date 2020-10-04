
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
        bold = workbook.add_format({'bold': True,'border':7,'bg_color':'#6F856D','align': 'center' })
        break_line = workbook.add_format({'bold': False,'border':7,'bg_color':'blue','align': 'center' })
        unbold = workbook.add_format({'bold': False,'border':7,'align': 'center'})
        datetime_style = workbook.add_format({'text_wrap': True,'border':7, 'num_format': 'dd-mm-yyyy','align': 'center'})
        date_from = data["form"]["date_from"]
        date_to = data["form"]["date_to"]
        customer = data["form"]["customer"]
        domain=[]
        if date_from:
            domain.append(('customer_order_delivery_date','>=',date_from))
        if date_to:
            domain.append(('customer_order_delivery_date', '<=', date_to))
        if customer:
            report_name= self.env['res.partner'].search([('id','=',customer)]).name
            ids=[]
            ids.append(customer)
            partner_ids = self.env['res.partner'].search([('parent_id','=',customer)])
            for rec in partner_ids:
                ids.append(rec.id)
            domain.append(('partner_id', 'in', ids))
        sheet.write(1, 2, 'Customer', bold)

        sheet.write(1, 3, 'Date', bold)
        sheet.write(1, 4, 'So', bold)
        sheet.write(1, 5, 'Item', bold)
        sheet.write(1, 6, 'Q', bold)
        sheet.write(1, 7, 'Price', bold)
        sheet.write(1, 8, 'Value', bold)
        sheet.write(1, 9, 'Amount After Vat', bold)
        row = 2
        col = 2
        sale_order = self.env['sale.order'].search(domain,order='customer_order_delivery_date asc')
        partner_ids=[]
        ids=[]
        for rec in sale_order:
            partner_ids.append(rec.partner_id)
            ids.append(rec.id)
        total,total_sub=0,0
        domain=[]
        for part in partner_ids:

                  so_id = sale_order.search([('partner_id','=',part.id),('id','in',ids)],order='customer_order_delivery_date asc')
                  totol_customer,totol_customer_sub = 0,0
                  for record in so_id:

                        col = 2

                        for rec in record.order_line:
                            totol_customer+=rec.price_total
                            totol_customer_sub+=rec.price_subtotal
                            total += rec.price_total
                            total_sub += rec.price_subtotal

                            if col ==2 :
                                sheet.write(row, 2, record.partner_id.name, unbold)
                            else:
                                sheet.write(row, 2, '', unbold)
                            # if record.partner_id.region_id:
                            #     sheet.write(row, 3, record.partner_id.region_id.name, unbold)
                            # else:
                            #     sheet.write(row, 3 , '', unbold)

                            if col == 2:

                               if record.customer_order_delivery_date:
                                    sheet.write(row, 3, record.customer_order_delivery_date, datetime_style)
                               else:
                                   sheet.write(row, 3, '', unbold)

                               sheet.write(row, 4, record.name, unbold)
                            else:


                                sheet.write(row, 4 , '', unbold)

                            sheet.write(row, 5, rec.product_id.name, unbold)
                            sheet.write(row, 6, rec.product_uom_qty, unbold)
                            sheet.write(row, 7, rec.price_unit, unbold)
                            sheet.write(row, 8, rec.price_subtotal, unbold)
                            sheet.write(row, 9, rec.price_total, unbold)

                            row+=1
                            col=3
                  sheet.write(row, 8, totol_customer_sub, break_line)
                  sheet.write(row, 9, totol_customer, break_line)
                  row+=1
        row+=1
        sheet.write(row, 8, total_sub, break_line)
        sheet.write(row, 9, total, break_line)


        row += 1




