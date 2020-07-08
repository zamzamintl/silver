
{
    'name': 'create activity when create ticket from lead  ',
    'version': '1.3',
    'category': 'Crm',
    'description': """create activity when create ticket from lead
""",
    'depends': ['crm','crm_helpdesk_custom_lead'],
    'data': ['views/activity.xml'],
     
    'installable': True,
    'auto_install': True,
}
