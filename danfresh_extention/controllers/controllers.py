# -*- coding: utf-8 -*-
from odoo import http

# class DanfreshExtention(http.Controller):
#     @http.route('/danfresh_extention/danfresh_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/danfresh_extention/danfresh_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('danfresh_extention.listing', {
#             'root': '/danfresh_extention/danfresh_extention',
#             'objects': http.request.env['danfresh_extention.danfresh_extention'].search([]),
#         })

#     @http.route('/danfresh_extention/danfresh_extention/objects/<model("danfresh_extention.danfresh_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('danfresh_extention.object', {
#             'object': obj
#         })