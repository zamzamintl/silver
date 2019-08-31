# -*- coding: utf-8 -*-
{
    'name': 'Show Product Images',
    'summary': 'Shows product images',
    'version': '12.0.1',
    'category': 'extra',
    'author': 'Mahmoud Ramadan',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['product', 'sale_management', 'purchase', 'account', 'mrp', 'stock'],
    'data': [
        'views/sale_order_line_images.xml',
        'views/mrp_order_line_images.xml',
        'views/purchase_order_line_images.xml',
        'views/invoice_order_line_images.xml',
        'views/stock_order_line_images.xml',
        'views/product_template.xml',
        'views/product_product.xml',
    ],
}
