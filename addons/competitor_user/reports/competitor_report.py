
from odoo import api, fields, models

class ReportProductSale(models.AbstractModel):
    _name = "report.competitor_user.competitor_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        creation_date = data["form"]["creation_date"]
        competitor_id = data["form"]["competitor_id"]
        sale_order_id = data["form"]["sale_order_id"]
        price_list = data["form"]["price_list"]
        domain=[]
        dates = []

        if creation_date:
            domain.append(('creation_date','=',creation_date))
        if competitor_id:
            domain.append(('person_competitor_id.competitor_id','=',competitor_id))
        lines = self.env['person.competitor.line'].search(domain,order='product_id asc')
        comp_lines=[]
        for lin in lines:
            comp_lines.append(lin.id)
            if lin.person_competitor_id.creation_date not in dates:
                dates.append(lin.person_competitor_id.creation_date)

        # sale_order = self.env['sale.order'].search([('id','=',sale_order_id)])
        # price_list = self.env['product.pricelist'].search([('id','=',price_list)])
        #
        # lst=[]
        # for record in sale_order.order_line:
        #     comp_ids = lines.search([('product_id','=',record.product_id.id)])
        #     if comp_ids:
        #         for comp_id in comp_ids:
        #              lst.append({'creation_date':comp_id.person_competitor_id.creation_date,'product_id':comp_id.product_id,
        #                    'competitor_id':comp_id.person_competitor_id.competitor_id,'competitor_price':comp_id.competitor_price,'my_price':record.price_unit })

        lst = []
        pro_list = []
        price_lst = self.env['product.pricelist.item'].search([('pricelist_id', '=', price_list)])
        print("sss", price_lst)
        for comp_id in lines:


            for plt in price_lst:
                print("1",plt.product_id)
                print("2", comp_id.product_id.id)
                print("1",plt.product_tmpl_id)
                print("2", comp_id.product_id.product_tmpl_id.id)


                if plt.product_id.id==comp_id.product_id.id and plt.product_id:

                    lst.append(
                        {'creation_date': comp_id.person_competitor_id.creation_date, 'product_id': comp_id.product_id,
                         'competitor_id': comp_id.person_competitor_id.competitor_id,
                         'competitor_price': comp_id.competitor_price, 'my_price': plt.price})
                elif plt.product_tmpl_id and plt.product_tmpl_id.id==comp_id.product_id.product_tmpl_id.id:

                    for rec in plt.product_tmpl_id.product_variant_ids:
                        pro_name = rec
                    lst.append(
                        {'creation_date': comp_id.person_competitor_id.creation_date,
                         'product_id': pro_name,
                         'competitor_id': comp_id.person_competitor_id.competitor_id,
                         'competitor_price': comp_id.competitor_price, 'my_price': plt.price})

        lst = sorted(lst, key=lambda i: (i['product_id'], i['my_price']))
        return {
            "doc_ids": data["ids"],
            "doc_model": data["model"],
            'lines':lst,
            'dates':dates
        }

