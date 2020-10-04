
from odoo import api, fields, models

class ReportProductSale(models.AbstractModel):
    _name = "report.competitor_user.competitor_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        creation_date = data["form"]["creation_date"]
        competitor_id = data["form"]["competitor_id"]
        sale_order_id = data["form"]["sale_order_id"]
        domain=[]
        dates = []

        if creation_date:
            domain.append(('creation_date','=',creation_date))
        if competitor_id:
            domain.append(('person_competitor_id','in',competitor_id))
        lines = self.env['person.competitor.line'].search(domain,order='product_id asc')

        for lin in lines:
            if lin.person_competitor_id.creation_date not in dates:
                dates.append(lin.person_competitor_id.creation_date)
        print(dates)
        print(lines)
        sale_order = self.env['sale.order'].search([('id','=',sale_order_id)])

        lst=[]
        for record in sale_order.order_line:
            comp_ids = lines.search([('product_id','=',record.product_id.id)])
            if comp_ids:
                for comp_id in comp_ids:
                     lst.append({'creation_date':comp_id.person_competitor_id.creation_date,'product_id':comp_id.product_id,
                           'competitor_id':comp_id.person_competitor_id.competitor_id,'competitor_price':comp_id.competitor_price,'my_price':record.price_unit })





        print(lines)
        return {
            "doc_ids": data["ids"],
            "doc_model": data["model"],
            'lines':lst,
            'dates':dates
        }

