# -*- coding: utf-8 -*-
{
    'name': "Product Pricing Access Permission",

    'summary': "Hide Cost / Sale Price",

    'author': "TopERP Technology Solution Limited, Linh Nguyen",
    'website': "https://toperp.vn/addons/product-price-permission",

    'category': 'Extra Tools',
    'version': '1.0',

    'depends': ['mail', 'product'],

    'data': [
        'views/product.xml',
        'data/groups.xml',
    ],
    'images': ['static/description/icon.png'],

    'license ': 'LGPL-3',

    'installable': True,
    'auto_install': False,
    'application': True,
}
