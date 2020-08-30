
{
    'name': 'Ecommerace custom',
    'version': '1.3',
    'category': 'sale',
    'description': """
e-commerance
===================================================
""",
    'depends': ['website_sale','sale','website_customer_order_delivery_date'],
    'data': ['views/partner.xml','views/templet_ecommerce.xml','views/action_view.xml','views/menu.xml','views/region_view.xml','views/search_view.xml','views/shipping.xml','secuirty/ir.model.access.csv'],
     
    'installable': True,
    'auto_install': True,
}
