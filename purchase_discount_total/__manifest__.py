# -*- coding: utf-8 -*-

{
    'name': 'Purchase Discount on Total Amount',
    'version': '12.0.1.1.0',
    'category': 'Purchase Management',
    'summary': "Discount on Total in Purchase and Invoice With Discount Limit and Approval",
    'author': '',
    'company': '',
    'website': '',
    'description': """

Purchase Discount for Total Amount
=======================
Module to manage discount on total amount in Purchase
        as an specific amount or percentage
""",
    'depends': ['purchase',
                'account'
                ],
    'data': [
        'views/purchase_view.xml',
        'views/account_invoice.xml',
        'views/invoice_report.xml',
        'views/purchase_report.xml',
    ],
    'demo': [
    ],
    'images': [''],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}
