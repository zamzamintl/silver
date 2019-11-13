# -*- coding: utf-8 -*-
{
    'name': "Danfresh Hr Customizations",
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
    'depends': ['base',
                'hr_expense',
                'hr_payroll_account'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/expense_template.xml',
        'views/hr_payroll_view.xml',
        'views/hr_employee_view.xml'
    ],
}
