{
    'name': 'procurements stock',
    'version': '12.0.1',
    'summary': 'procurements stock stop cron job ',
    'sequence': 19,
    'category': 'inventory',
    'author': 'Mohamed Abd El Rahman',
    'description': """
   stop cron job running reservation
    """,
    'depends': [ 'stock'],


    'installable': True,
    'application': True,
    'auto_install': False,
}