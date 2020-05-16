# -*- coding: utf-8 -*-
# from odoo import http


# class HdlUpdateRes.partner(http.Controller):
#     @http.route('/hdl_update_res.partner/hdl_update_res.partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hdl_update_res.partner/hdl_update_res.partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hdl_update_res.partner.listing', {
#             'root': '/hdl_update_res.partner/hdl_update_res.partner',
#             'objects': http.request.env['hdl_update_res.partner.hdl_update_res.partner'].search([]),
#         })

#     @http.route('/hdl_update_res.partner/hdl_update_res.partner/objects/<model("hdl_update_res.partner.hdl_update_res.partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hdl_update_res.partner.object', {
#             'object': obj
#         })
