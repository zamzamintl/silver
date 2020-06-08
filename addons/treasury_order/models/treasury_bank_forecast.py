# Copyright 2018 Giacomo Grasso <giacomo.grasso.82@gmail.com>
# Odoo Proprietary License v1.0 see LICENSE file

import ast
from odoo import models, fields, api, exceptions, _


class BankBalanceComputation(models.TransientModel):
    _inherit = "bank.balance.computation"

    include_sale_orders = fields.Boolean(string='Incl. SO')
    include_purchase_orders = fields.Boolean(string='Incl. PO')

    def get_so_query(self, date_start, date_end, company_domain):
        query = """
                UNION

                SELECT CAST('SO' AS text) AS type, so.id AS ID, so.treasury_date, so.name, so.company_id,
                    so.amount_main_currency as amount, NULL AS cf_forecast, NULL AS journal_id
                FROM sale_order so
                WHERE so.treasury_date BETWEEN '{}' AND '{}'
                    AND so.state NOT IN ('cancel') 
                    AND so.company_id in {}
            """.format(date_start, date_end, company_domain)
        return query

    def get_po_query(self, date_start, date_end, company_domain):
        query = """
                UNION

                SELECT CAST('PO' AS text) AS type, po.id AS ID, po.treasury_date, po.name, po.company_id,
                    - po.amount_main_currency as amount, NULL AS cf_forecast, NULL AS journal_id
                FROM purchase_order po
                WHERE po.treasury_date BETWEEN '{}' AND '{}'
                    AND po.state NOT IN ('cancel') 
                    AND po.company_id in {}
            """.format(date_start, date_end, company_domain)
        return query

    def _get_additional_subquery(self, fc_journal_list, date_start, date_end):
        additional_subquery = super(BankBalanceComputation, self)._get_additional_subquery(
            fc_journal_list, date_start, date_end)
        company_domain = tuple([self.env.user.company_id.id]*2)

        if self.include_sale_orders:
            additional_subquery += self.get_so_query( date_start, date_end, company_domain)

        if self.include_purchase_orders:
            additional_subquery += self.get_po_query(date_start, date_end, company_domain)

        return additional_subquery

