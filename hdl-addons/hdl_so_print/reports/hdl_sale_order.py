from odoo import models, fields, api

class ReportProductSale(models.AbstractModel):
    _name = "report.hdl_so_print.hdl_sale_order"

    @api.model
    def _get_report_values(self, docids, data=None):
        print("ddfdfdfdfdfd")