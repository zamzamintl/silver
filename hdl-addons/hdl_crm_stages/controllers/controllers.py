# -*- coding: utf-8 -*-
# from odoo import http


# class HdlCrmStages(http.Controller):
#     @http.route('/hdl_crm_stages/hdl_crm_stages/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hdl_crm_stages/hdl_crm_stages/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hdl_crm_stages.listing', {
#             'root': '/hdl_crm_stages/hdl_crm_stages',
#             'objects': http.request.env['hdl_crm_stages.hdl_crm_stages'].search([]),
#         })

#     @http.route('/hdl_crm_stages/hdl_crm_stages/objects/<model("hdl_crm_stages.hdl_crm_stages"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hdl_crm_stages.object', {
#             'object': obj
#         })
