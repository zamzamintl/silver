# -*- coding: utf-8 -*-
{
    'name': "Danfresh",

    'summary': """
        
        """,

    'description': """
    This Module Feature is:\n
        1-Recurring Expenses.\n
          
    """,

    'author': "Odoo Mates",
    'website': "http://www.yourcompany.com",

    
    'category': 'hr',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_expense'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/expense_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
