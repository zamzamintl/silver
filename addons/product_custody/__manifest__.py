# -*- coding: utf-8 -*-
{
	'name': 'Product custody',
	'version': '12.0.1.0.0',
	'summary': 'edite starting date for working days',
	'category': 'hr',
	'author': 'Emad Raafat',
	'maintainer': 'unicom Techno Solutions',
	'company': 'unicom group Solutions',
	'website': 'https://www.unicom.com',
	'depends': ['base','hr','product','stock'],
	'data': [
		'security/equipment_security.xml',
		'security/ir.model.access.csv',
		'views/product_custody.xml',
		'views/product_custody_reconcile.xml',
		'views/employee_custody.xml',
		'views/sh_message_wizard.xml',
		'views/stock_operation_type.xml',
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': True,
	'auto_install': False,
	'sequence':1
}
