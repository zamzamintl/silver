# -*- coding: utf-8 -*-
{
    'name': "Silver Partner Updates",

    'summary': """
       """,

    'description': """
        Long description of module's purpose
    """,


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','documents'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/document_view.xml',
    ],

}