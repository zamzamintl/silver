# -*- coding: utf-8 -*-
{
    'name': "Prevent Create New Contact from Order Form",

    'summary': """
        Prevent users to create new contact from the order form
        """,

    'description': """
        Sometimes a user accidentally created duplicate contact from order form such from the sales.order or purchase.order form.
        using this module we can prevent users make the mistakes
    """,

    'author': "Lima Bersaudara",
    'website': "http://github.com/trinanda",
    'images': ['static/description/icon.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Utilities',
    'version': '13.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/purchase_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
