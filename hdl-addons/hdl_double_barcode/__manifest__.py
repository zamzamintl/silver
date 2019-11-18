# -*- coding: utf-8 -*-
{
    'name': "Double Barcode",
    'summary': """Each product has two barcode""",
    'description': """
    
    """,

    'author': "Plementus By Mario Roshdy",
    'website': "https://plementus.com",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}