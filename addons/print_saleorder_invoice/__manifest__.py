# -*- coding: utf-8 -*-
{
    'name': "Print Sales Order and invoice ",

    'summary': """ change print of sales order and invoice """,

    'description': """change print of sales order and invoice

    """,

    'author': "Mohamed abd elrhman 01128218762",
    'website': "",

    
    'category': 'sales',
    'version': '13.0.1.1',
    'depends': ['base', 'account','ecomm_custom'],

    # always loaded
    'data': ['views/sale_order_print.xml'
    ],
    'qweb': [],
    
    'demo': [],
    'application': True,

}
