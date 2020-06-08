# -*- coding: utf-8 -*-
{
    'name': "Product Sale Price History",

    'summary': """
        This module useful to show history of sale price for product, 
        you can also track history of sale price of product for different customers.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HCS",
    'website': "http://hcsgroup.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
}
