# -*- coding: utf-8 -*-
{
    'name': "Silver Sale Updates",

    'summary': """  add code have sequence of lead at CRM ,
	     add hieght and wights at product ,,add tag in product 
		 -
       """,

    'description': """
    """,

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','crm','stock'],

    'data': [
        'security/ir.model.access.csv',
        'data/crm_lead_sequence.xml',
        'views/crm_view.xml',
        'views/product_view.xml'
    ],

}