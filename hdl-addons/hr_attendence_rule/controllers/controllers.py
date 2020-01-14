# -*- coding: utf-8 -*-
# from odoo import http


# class HrAttendenceRule(http.Controller):
#     @http.route('/hr_attendence_rule/hr_attendence_rule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_attendence_rule/hr_attendence_rule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_attendence_rule.listing', {
#             'root': '/hr_attendence_rule/hr_attendence_rule',
#             'objects': http.request.env['hr_attendence_rule.hr_attendence_rule'].search([]),
#         })

#     @http.route('/hr_attendence_rule/hr_attendence_rule/objects/<model("hr_attendence_rule.hr_attendence_rule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_attendence_rule.object', {
#             'object': obj
#         })
