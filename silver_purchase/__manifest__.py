# -*- coding: utf-8 -*-
{
    'name': "silver_purchase",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ramadan Khalil",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','purchase','alan_customize','stock'],

    'data': [
        'views/purchase_view.xml',
        'views/purchase_report_template.xml'
    ],

}