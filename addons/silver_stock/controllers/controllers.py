# -*- coding: utf-8 -*-
from odoo import http

# class SilverStock(http.Controller):
#     @http.route('/silver_stock/silver_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/silver_stock/silver_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('silver_stock.listing', {
#             'root': '/silver_stock/silver_stock',
#             'objects': http.request.env['silver_stock.silver_stock'].search([]),
#         })

#     @http.route('/silver_stock/silver_stock/objects/<model("silver_stock.silver_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('silver_stock.object', {
#             'object': obj
#         })