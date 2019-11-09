# -*- coding: utf-8 -*-
{
    'name': "Danfresh Accounting Customizations",
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
                'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/invoice_view.xml',
        'report/account_invoice_report_templates.xml',
        'report/account_invoice_report_view.xml'
    ],
}
