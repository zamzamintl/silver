from odoo import http
from odoo.http import request
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo.addons.note.controllers.note import NoteController
class Note(NoteController):

    @http.route('/note/new', type='json', auth='user')
    def note_new_from_systray(self, note, activity_type_id=None, date_deadline=None):
        _logger.info("NOTENOTE")
        """ Route to create note and their activity directly from the systray """
        note = request.env['note.note'].create({'name': note})
        _logger.info(note.name)
        if date_deadline:
            activity_values = {
                'note': note.name,
                'date_deadline': date_deadline,
                'res_model_id': request.env.ref("note.model_note_note").id,
                'res_id': note.id,
                'note_id': note.id,
            }
            if not activity_type_id:
                activity_type_id = request.env['mail.activity.type'].sudo().search([('category', '=', 'reminder')], limit=1).id
            if activity_type_id:
                activity_values['activity_type_id'] = activity_type_id
            request.env['mail.activity'].create(activity_values)
        return note.id