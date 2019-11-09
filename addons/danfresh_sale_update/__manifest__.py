# -*- coding: utf-8 -*-
{
    'name': "Danfresh CRM & Sales Customizations",
    'summary': """
    """,
    'description': """
    """,
    'author': 'Plementus',
    'website': 'https://www.plementus.com',

    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
    ],
    'version': '0.1',
    'depends': ['base',
                'crm',
                'sale_management',
                'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'data/ir_sequence.xml',
        'views/sale_order.xml',
        'views/product_view.xml',
        'views/res_partner_views.xml',
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
        'views/opportunity_type.xml'

    ],
}
