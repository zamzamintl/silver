# -*- coding: utf-8 -*-
from odoo import http

# class Danfresh(http.Controller):
#     @http.route('/danfresh/danfresh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/danfresh/danfresh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('danfresh.listing', {
#             'root': '/danfresh/danfresh',
#             'objects': http.request.env['danfresh.danfresh'].search([]),
#         })

#     @http.route('/danfresh/danfresh/objects/<model("danfresh.danfresh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('danfresh.object', {
#             'object': obj
#         })