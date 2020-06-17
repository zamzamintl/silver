# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Employee Numbering',
    'version': '1.0',
    'summary': 'Auto Genereate Employee Number for New Employees',
    'description': """
          add a field for genereting new Employee Number for new empoyee.
    """,
    'company': "PT. Artsys Integrasi Solusindo",
    'author': "PT. Artsys Integrasi Solusindo",
    'maintainer': "PT. Artsys Integrasi Solusindo",
    'website': "http://www.artsys.id",
    'category': 'HRMS - Human Resource Management System',

    'depends': ['hr'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/hr_views.xml',
    ],
    'css': [
    ],
    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
}
