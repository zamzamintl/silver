
from odoo import api, fields, models

class ReportProductSale(models.AbstractModel):
    _name = "report.competitor_user.competitor_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        creation_date = data["form"]["creation_date"]
        competitor_id = data["form"]["competitor_id"]
        domain=[]

        if creation_date:
            domain.append(('person_competitor_id.creation_date','=',creation_date))
        if competitor_id:
            domain.append(('person_competitor_id','in',competitor_id))
        lines = self.env['person.competitor.line'].search(domain,order='product_id asc')
        products=[]
        for lin in lines:
            if lin.person_competitor_id.creation_date not in  products:
                  products.append(lin.person_competitor_id.creation_date)



        print(lines)
        return {
            "doc_ids": data["ids"],
            "doc_model": data["model"],
            'lines':lines,
            'products':products
        }

