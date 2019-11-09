# -*- coding: utf-8 -*-
{
    'name': "Danfresh Activity Customizations",
    'summary': """
    """,
    'description': """
    """,
    'author': 'Plementus',
    'website': 'https://www.plementus.com',

    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
    ],
    'version': '0.1',
    'depends': ['base',],
    'data': [
        'security/ir.model.access.csv',
        'views/mail_activity.xml',
        'views/web_assets.xml'


    ],
    'qweb': [
        'static/src/xml/sysactivity.xml',

    ]
}
