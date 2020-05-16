# -*- coding: utf-8 -*-
{
    'name': "Product & Quotation Tracking",

    'summary': """Product & Quotation Fields Tracking""",

    'description': """
        Product & Quotation Fields Tracking
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'base',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'membership', 'crm', 'sale', 'purchase', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
