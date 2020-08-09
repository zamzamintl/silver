# -*- coding: utf-8 -*-
# from odoo import http


# class SaleTeamCustom(http.Controller):
#     @http.route('/sale_team_custom/sale_team_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_team_custom/sale_team_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_team_custom.listing', {
#             'root': '/sale_team_custom/sale_team_custom',
#             'objects': http.request.env['sale_team_custom.sale_team_custom'].search([]),
#         })

#     @http.route('/sale_team_custom/sale_team_custom/objects/<model("sale_team_custom.sale_team_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_team_custom.object', {
#             'object': obj
#         })
