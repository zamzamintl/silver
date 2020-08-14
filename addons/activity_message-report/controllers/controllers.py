# -*- coding: utf-8 -*-
# from odoo import http


# class ActivityMessage-report(http.Controller):
#     @http.route('/activity_message-report/activity_message-report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/activity_message-report/activity_message-report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('activity_message-report.listing', {
#             'root': '/activity_message-report/activity_message-report',
#             'objects': http.request.env['activity_message-report.activity_message-report'].search([]),
#         })

#     @http.route('/activity_message-report/activity_message-report/objects/<model("activity_message-report.activity_message-report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('activity_message-report.object', {
#             'object': obj
#         })
