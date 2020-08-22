# -*- coding: utf-8 -*-
{
    'name': "secreen_view",

    'summary': """
        screen view and access right """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohamed Abd El rahman",
    'website': "",


    'category': 'inventroy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/user_group.xml',
        'views/actions.xml',
        'views/views.xml',
        'views/menu.xml',

    ],

}
