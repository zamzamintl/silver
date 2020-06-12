{
    'name': "Products and Quantity on Sales Order",
    'author': 'Ascetic Business Solution',
    'category': 'Sales',
    'summary': """Display Products and Quantity on Sales Order and Printed Report""",
    'license': 'AGPL-3',
    'website': 'http://www.asceticbs.com',
    'description': """
""",
    'version': '13.0.1.0',
    'depends': ['base','sale_management'],
    'data': ['security/sale_order_security.xml', 
             'views/sale_order_view.xml',
             'report/sale_report_templates.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
