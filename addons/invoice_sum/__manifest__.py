
{
    'name': 'Invoice Sum Quantity',
    'version': '1.3',
    'category': 'account',
    'description': """
Sum quantity of some of invoice line
===================================================
""",
    'depends': ['sale'],
    'data': ['views/report_action.xml','views/tempalet_sum_order.xml'],
     
    'installable': True,
    'auto_install': True,
}
