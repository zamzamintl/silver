# -*- coding: utf-8 -*-
# from odoo import http


# class SecreenView(http.Controller):
#     @http.route('/secreen_view/secreen_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/secreen_view/secreen_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('secreen_view.listing', {
#             'root': '/secreen_view/secreen_view',
#             'objects': http.request.env['secreen_view.secreen_view'].search([]),
#         })

#     @http.route('/secreen_view/secreen_view/objects/<model("secreen_view.secreen_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('secreen_view.object', {
#             'object': obj
#         })
