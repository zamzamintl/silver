# -*- coding: utf-8 -*-
{
    'name': "Danfresh Extention",

    'summary': """Danfresh Extention""",

    'description': """
        Danfresh Extention
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sale', 'sale_management', 'mail','project','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/crm_lead_view_inh.xml',
        'views/my_assets.xml',
        'views/opportunity_type.xml',
        'views/sale_inh.xml',
        'views/res_user_inh.xml',
        'report/ifoora.xml',
        'report/quantity_only.xml',
        'report/without_tax.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/mail_activity.xml',
    ],
    'qweb': [
        'static/src/xml/sysactivity.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
