# -*- coding: utf-8 -*-
from odoo import http

# class SilverDoubleBarcode(http.Controller):
#     @http.route('/silver_double_barcode/silver_double_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silver_double_barcode/silver_double_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('silver_double_barcode.listing', {
#             'root': '/silver_double_barcode/silver_double_barcode',
#             'objects': http.request.env['silver_double_barcode.silver_double_barcode'].search([]),
#         })

#     @http.route('/silver_double_barcode/silver_double_barcode/objects/<model("silver_double_barcode.silver_double_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silver_double_barcode.object', {
#             'object': obj
#         })