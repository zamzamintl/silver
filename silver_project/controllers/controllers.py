# -*- coding: utf-8 -*-
from odoo import http

# class SilverProject(http.Controller):
#     @http.route('/silver_project/silver_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silver_project/silver_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('silver_project.listing', {
#             'root': '/silver_project/silver_project',
#             'objects': http.request.env['silver_project.silver_project'].search([]),
#         })

#     @http.route('/silver_project/silver_project/objects/<model("silver_project.silver_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silver_project.object', {
#             'object': obj
#         })