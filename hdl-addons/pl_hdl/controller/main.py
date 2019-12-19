import json
from odoo import http, _
from odoo.http import request


class PlHDL(http.Controller):

    @http.route(['/', ],
                type='http', auth="public", website=True, sitemap=False)
    def home(self, **kw):
        return request.render("pl_hdl.home", {'pageName': 'homepage'})

    @http.route(['/products', ],
                type='http', auth="public", website=True, sitemap=False)
    def products(self, **kw):
        return request.render("pl_hdl.products", {'pageName': 'products'})

    @http.route(['/news', ],
                type='http', auth="public", website=True, sitemap=False)
    def news(self, **kw):
        return request.render("pl_hdl.news", {'pageName': 'news'})

    @http.route(['/partners', ],
                type='http', auth="public", website=True, sitemap=False)
    def partners(self, **kw):
        return request.render("pl_hdl.partners", {'pageName': 'partners'})

    @http.route(['/commercial', ],
                type='http', auth="public", website=True, sitemap=False)
    def commercial(self, **kw):
        return request.render("pl_hdl.commercial", {'pageName': 'commercial'})

    @http.route(['/residential', ],
                type='http', auth="public", website=True, sitemap=False)
    def residential(self, **kw):
        return request.render("pl_hdl.residential", {'pageName': 'residential'})

    @http.route(['/hotels', ],
                type='http', auth="public", website=True, sitemap=False)
    def hotels(self, **kw):
        return request.render("pl_hdl.hotels", {'pageName': 'hotels'})

    @http.route(['/about', ],
                type='http', auth="public", website=True, sitemap=False)
    def about(self, **kw):
        return request.render("pl_hdl.about", {'pageName': 'about'})

    @http.route(['/case_studies', ],
                type='http', auth="public", website=True, sitemap=False)
    def case_studies(self, **kw):
        return request.render("pl_hdl.case_studies", {'pageName': 'case_studies'})

    @http.route(['/modern_chalet', ],
                type='http', auth="public", website=True, sitemap=False)
    def modern_chalet(self, **kw):
        return request.render("pl_hdl.modern_chalet", {'pageName': 'modern_chalet'})

    @http.route(['/thanks_page', ],
                type='http', auth="public", website=True, sitemap=False)
    def thanks_page(self, **kw):
        return request.render("pl_hdl.thanks_page", {'pageName': 'thanks_page'})
