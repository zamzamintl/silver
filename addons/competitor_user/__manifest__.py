# -*- coding: utf-8 -*-
{
    'name': "competitor User",
    'description': """
       person competitor
    """,

    'author': "Moahemd abd El Rahman",



    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','ecomm_custom'],

    # always loaded
    'data': [

        'views/views.xml',

        'wizard/wizard_form.xml',
         'views/competitor_report.xml',
         'security/groups_user.xml',
        'security/ir.model.access.csv',
        'views/http_competitor.xml'

    ],

}