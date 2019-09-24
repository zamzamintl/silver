# -*- coding: utf-8 -*-
from odoo import http

# class SilverAccount(http.Controller):
#     @http.route('/silver_account/silver_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silver_account/silver_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('silver_account.listing', {
#             'root': '/silver_account/silver_account',
#             'objects': http.request.env['silver_account.silver_account'].search([]),
#         })

#     @http.route('/silver_account/silver_account/objects/<model("silver_account.silver_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silver_account.object', {
#             'object': obj
#         })