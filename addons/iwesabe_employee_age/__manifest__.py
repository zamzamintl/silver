# -*- coding: utf-8 -*-
{
    'name': 'Employee Age',
    'version': '13.0.1.0',
    'author': 'iWesabe',
    'summary': 'Employee age and birthday wishes',
    'description': """This module shows employee age in employee form and send birthday wishes to employees""",
    'category': 'Human Resources',
    'website': 'https://www.iwesabe.com/',
    'license': 'AGPL-3',

    'depends': ['hr'],

    'data': [
        'data/mail_template_data.xml',
        'data/birthday_cron_data.xml',
        'views/hr_employee_views.xml',
    ],

    'qweb': [],
    'images': ['static/description/iWesabe-Apps-EmployeeAge.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
}
