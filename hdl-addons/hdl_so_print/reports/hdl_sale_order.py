from odoo import models, fields, api

class ReportProductSale(models.AbstractModel):
    _name = "report.hdl_so_print.hdl_sale_order"

    @api.model
    def _get_report_values(self, docids, data=None):

        sales_order = self.env['sale.order'].search([('id','in',docids)])
        product_cate_id,lines,survey=[],[],[]
        for rec in sales_order:
            if rec.survey_sheet:
                survey.append(rec.survey_sheet)

        for line in sales_order.order_line:

            if line.product_id.categ_id.visible == False:
                catg_id=line.product_id.categ_id
                check=False
                save_category=0

                while (check ==False):

                    if catg_id.parent_id.visible == True  :
                        check=True

                    if catg_id.parent_id.visible == True and catg_id.parent_id:
                        if catg_id.parent_id not in product_cate_id:
                            product_cate_id.append(catg_id.parent_id)
                        save_category =catg_id.parent_id
                    else:
                        if catg_id.parent_id:
                              catg_id=catg_id.parent_id
            else:
                 save_category=line.product_id.categ_id
                 if line.product_id.categ_id not in product_cate_id:
                        product_cate_id.append(line.product_id.categ_id)
            values={'categ_id':save_category,'product_id':line.product_id,'product_uom_qty':line.product_uom_qty,'price_unit':line.price_unit,
                    'discount':line.discount,'price_subtotal':line.price_subtotal,'price_total':line.price_total,'order_id':line.order_id,'name':line.name,'tax_id':line.tax_id}
            lines.append(values)
        print(product_cate_id)
        print(lines)
        return {
            'docs': sales_order,
            'doc_model': 'sale.order',
            'lines': lines,
            'product_cate_id': product_cate_id,
            'survey':survey,


            'proforma': True
        }