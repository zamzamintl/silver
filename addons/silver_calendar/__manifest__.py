# -*- coding: utf-8 -*-
{
    'name': "silver_calendar",

    'summary': """
        add time and note when create event """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    'data': [
        'security/ir.model.access.csv',
        'views/calendar_view.xml',

    ],

}