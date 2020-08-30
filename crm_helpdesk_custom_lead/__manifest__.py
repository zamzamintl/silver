
{
    'name': 'helpdesk  & crm custom ',
    'version': '1.3',
    'category': 'helpdesk',
    'description': """create sales order from ticket  and relate between ticket and lead 
""",
    'depends': ['crm', 'helpdesk','crm_helpdesk','sale','base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'fetchmail',
        'utm',
        'sale_crm',
        'web_tour',
        'contacts',
        'digest',
        'phone_validation',],
    'data': ['views/ticket_sale.xml','views/survey_sheet.xml','secuirty/ir.model.access.csv','views/menus.xml',
             'views/surevy_sheet_report.xml',"views/sale_order.xml"],
     
    'installable': True,
    'auto_install': True,
}
