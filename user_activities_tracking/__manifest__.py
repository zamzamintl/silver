# -*- coding: utf-8 -*-
{
    'name': "User Activities Tracking",

    'summary': """
        The module will Track users Activities""",

    'description': """
        The module will Track users Activities""",

    'author': "Mahmoud Ramdan",
    'website': "",
    'category': 'web',
    'version': '12.0.1',
    'license': "AGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/user_log_security.xml',
        'security/ir.model.access.csv',
        'views/user_activity_view.xml',
        'views/custom_xml.xml',

    ],
    'qweb': ['static/src/xml/user_menu_template.xml'],
    'installable': True,
    'application': True
}
