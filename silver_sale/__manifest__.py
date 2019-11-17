# -*- coding: utf-8 -*-
{
    'name': "Silver Sale Updates",


    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','crm','stock','sale','alan_customize'],

    'data': [
        'security/ir.model.access.csv',
        'data/crm_lead_sequence.xml',
        'views/sale_view.xml',
        'views/crm_view.xml',
        'views/product_view.xml',
        'views/sale_report_template.xml',
        'report/sale_sum_report.xml',
        'views/res_partner_views.xml'
    ],

}