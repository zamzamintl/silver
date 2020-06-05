
{
    'name': 'helpdesk  & crm custom ',
    'version': '1.3',
    'category': 'helpdesk',
    'description': """create sales order from ticket  and relate between ticket and lead 
""",
    'depends': ['crm', 'helpdesk','crm_helpdesk','sale'],
    'data': ['views/ticket_sale.xml','views/survey_sheet.xml','secuirty/ir.model.access.csv'],
     
    'installable': True,
    'auto_install': True,
}
