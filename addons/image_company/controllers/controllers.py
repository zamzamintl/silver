# -*- coding: utf-8 -*-
# from odoo import http


# class ImageCompany(http.Controller):
#     @http.route('/image_company/image_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/image_company/image_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('image_company.listing', {
#             'root': '/image_company/image_company',
#             'objects': http.request.env['image_company.image_company'].search([]),
#         })

#     @http.route('/image_company/image_company/objects/<model("image_company.image_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('image_company.object', {
#             'object': obj
#         })
