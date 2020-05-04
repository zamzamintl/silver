# Copyright 2018 Giacomo Grasso <giacomo.grasso.82@gmail.com>
# Odoo Proprietary License v1.0 see LICENSE file

{
    'name': 'Orders Cash Flow Management',
    'version': '12.0.1.0',
    'category': 'Accounting',
    'description': """
            Adding sale and purchase orders to the treasury and 
            cash flow management.
        """,
    'author': 'Giacomo Grasso - giacomo.grasso.82@gmail.com ',
    'maintainer': 'Giacomo Grasso - giacomo.grasso.82@gmail.com',
    'website': 'https://github.com/jackjack82',
    'images': ['static/description/main_screenshot.png'],
    'license': 'OPL-1',
    'currency': 'EUR',
    'depends': [
        'account',
        'sale_management',
        'purchase',
        'order_open_amount',
        'treasury_forecast',
        ],
    'data': [
        'views/order.xml',
        'views/treasury_forecast.xml',
        'views/treasury_bank_forecast.xml',

        'security/ir.model.access.csv',

    ],

    'installable': True,
    'auto_install': False,
}
