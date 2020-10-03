
{
    'name' : 'Sale report EXcel',
    'version' : '12.0.1',
    'summary': 'Module all Account product .',
    'sequence': 16,
    'category': 'Account',
    'author' : 'Mohamed Abd Elrhamn',
    'description': """
Custom Sales Report
=====================================
This module print daily, last week and last month sale report.
Also print report for particular duration.
    """,
    "license": "AGPL-3",
    'depends' : ['base_setup', 'sale_management','account'],
    'data': [
        'wizard/wiz_sale_report_view.xml',
        'views/sale_report_view.xml',
        'views/report_sale_report.xml'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
