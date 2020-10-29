import odoo.http as http

class Example(http.Controller):
    @http.route('/competitor', type='http', auth='public', website=True)
    def render_courses_page(self):
        competitor = http.request.env['res.competitor'].sudo().search([])

        return http.request.render('competitor_user.courses_page', {'competitor': competitor})