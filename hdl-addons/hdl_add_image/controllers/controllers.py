# -*- coding: utf-8 -*-
# from odoo import http


# class HdlAddImage(http.Controller):
#     @http.route('/hdl_add_image/hdl_add_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hdl_add_image/hdl_add_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hdl_add_image.listing', {
#             'root': '/hdl_add_image/hdl_add_image',
#             'objects': http.request.env['hdl_add_image.hdl_add_image'].search([]),
#         })

#     @http.route('/hdl_add_image/hdl_add_image/objects/<model("hdl_add_image.hdl_add_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hdl_add_image.object', {
#             'object': obj
#         })
