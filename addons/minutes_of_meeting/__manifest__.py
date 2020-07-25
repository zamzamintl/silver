
{
    'name': 'Agenda of Meetiong ',
    'version': '1.3',
    'category': 'sale',
    'description': """create agenda of meeting at calendar and save minutes  of meeting
""",
    'depends': ['calendar'],
    'author':'Mohamed Abd Elrhamn 01128218762',
    'data': ["views/agenda_action.xml","views/genda_menus.xml","views/agenda_form.xml","views/calendar.xml","security/ir.model.access.csv","views/report_minutes_of_meeting.xml"],
    'installable': True,
    'auto_install': True,
}
