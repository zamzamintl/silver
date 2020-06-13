from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery
import logging 
from odoo import fields, http, tools, _
from odoo.http import request
_logger = logging.getLogger(__name__)
from odoo import api, fields ,models
from odoo.exceptions import ValidationError 
from odoo.http import request
class website_cust(WebsiteSale):
    
    def values_postprocess(self, order, mode, values, errors, error_msg):
        _logger.info("values_postprocess")
        new_values = {}
        authorized_fields = request.env['ir.model']._get('res.partner')._get_form_writable_fields()
        for k, v in values.items():
            # don't drop empty value, it could be a field to reset
            if k=='mobile' or k=='floor'or k=='block' or k=='region_id' or k=='partition' or k=='district' :
                new_values[k] = v
            if k in authorized_fields and v is not None:
                new_values[k] = v
            else:  # DEBUG ONLY
                if k not in ('field_required', 'partner_id', 'callback', 'submitted'): # classic case
                    _logger.debug("website_sale postprocess: %s value has been dropped (empty or not writable)" % k)

        new_values['team_id'] = request.website.salesteam_id and request.website.salesteam_id.id
        new_values['user_id'] = request.website.salesperson_id and request.website.salesperson_id.id

        if request.website.specific_user_account:
            new_values['website_id'] = request.website.id

        if mode[0] == 'new':
            new_values['company_id'] = request.website.company_id.id

        lang = request.lang.code if request.lang.code in request.website.mapped('language_ids.code') else None
        if lang:
            new_values['lang'] = lang
        if mode == ('edit', 'billing') and order.partner_id.type == 'contact':
            new_values['type'] = 'other'
        if mode[1] == 'shipping':
            new_values['parent_id'] = order.partner_id.commercial_partner_id.id
            new_values['type'] = 'delivery'

        return new_values, errors, error_msg
     
    @http.route(['/add_all/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product_ppp(self, product, category='', search='',add_qty=1, **kwargs):
        _logger.info("Add NEW ")
        _logger.info(kwargs)
        _logger.info(product)
        product_twmp=request.env['product.product'].search([('product_tmpl_id','=',product.id)]).id
        _logger.info(product_twmp)
        self.cart_update(product_twmp)
        return request.redirect('/shop')
    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):
        _logger.info("address")
        _logger.info(kw)
        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
        _logger.info(Partner)
        order = request.website.sale_get_order()

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        mode = (False, False)
        can_edit_vat = False
        def_country_id = order.partner_id.country_id
        values, errors = {}, {}

        partner_id = int(kw.get('partner_id', -1))

        # IF PUBLIC ORDER
        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            mode = ('new', 'billing')
            can_edit_vat = True
            country_code = request.session['geoip'].get('country_code')
            if country_code:
                def_country_id = request.env['res.country'].search([('code', '=', country_code)], limit=1)
            else:
                def_country_id = request.website.user_id.sudo().country_id
        # IF ORDER LINKED TO A PARTNER
        else:
            if partner_id > 0:
                if partner_id == order.partner_id.id:
                    mode = ('edit', 'billing')
                    can_edit_vat = order.partner_id.can_edit_vat()
                else:
                    shippings = Partner.search([('id', 'child_of', order.partner_id.commercial_partner_id.ids)])
                    if partner_id in shippings.mapped('id'):
                        mode = ('edit', 'shipping')
                    else:
                        return Forbidden()
                if mode:
                    values = Partner.browse(partner_id)
            elif partner_id == -1:
                mode = ('new', 'shipping')
            else: # no mode - refresh without post?
                return request.redirect('/shop/checkout')

        # IF POSTED
        if 'submitted' in kw:
            _logger.info("submit")
            pre_values = self.values_preprocess(order, mode, kw)
            errors, error_msg = self.checkout_form_validate(mode, kw, pre_values)
            post, errors, error_msg = self.values_postprocess(order, mode, pre_values, errors, error_msg)

            if errors:
                errors['error_message'] = error_msg
                values = kw
            else:
                partner_id = self._checkout_form_save(mode, post, kw)
                if mode[1] == 'billing':
                    order.partner_id = partner_id
                    order.onchange_partner_id()
                    # This is the *only* thing that the front end user will see/edit anyway when choosing billing address
                    order.partner_invoice_id = partner_id
                    if not kw.get('use_same'):
                        kw['callback'] = kw.get('callback') or \
                            (not order.only_services and (mode[0] == 'edit' and '/shop/checkout' or '/shop/address'))
                elif mode[1] == 'shipping':
                    order.partner_shipping_id = partner_id

                order.message_partner_ids = [(4, partner_id), (3, request.website.partner_id.id)]
                if not errors:
                    return request.redirect(kw.get('callback') or '/shop/confirm_order')

        country = 'country_id' in values and values['country_id'] != '' and request.env['res.country'].browse(int(values['country_id']))
        country = country and country.exists() or def_country_id
        region_id=request.env['state.region1'].search([])
        #regions='region_id' in values and values['region_id'] != '' and request.env['res.country'].browse(int(values['state.region1']))
        region_id_2=request.env['state.region2'].search([])
        region_id_3=request.env['state.region'].search([])
        _logger.info("region1111")
        _logger.info(region_id)
        

        
        render_values = {
            'website_sale_order': order,
            'partner_id': partner_id,
            'mode': mode,
            'checkout': values,
            'can_edit_vat': can_edit_vat,
            'country': country,
            'countries': country.get_website_sale_countries(mode=mode[1]),
            "states": country.get_website_sale_states(mode=mode[1]),
            "district":[],
            'error': errors, 
             
            'callback': kw.get('callback'),
            'only_services': order and order.only_services,
        }
        return request.render("website_sale.address", render_values)
     
    def _get_mandatory_billing_fields(self):
        _logger.info("_get_mandatory_billing_fields")
        return ["name", "email", "street", "city", "country_id","floor","block","region_id","district","partition"]
    @http.route(['/shop/state_infos/<model("res.country.state"):state_id>'], type='json', auth="public", methods=['POST'], website=True)
    def state_infos(self, state_id, mode, **kw):
        _logger.info("state_infos")
        _logger.info(state_id)
        region_id_1=request.env['state.region1'].search([('state_id','=',state_id.id)])
        area=[(st.id, st.name, st.state_id) for st in region_id_1]
        _logger.info(area)
        
        _logger.info(region_id_1)
        return dict(
             
            region_id=area,
             
        )
    @http.route(['/shop/state_area/<model("state.region1"):region_id>'], type='json', auth="public", methods=['POST'], website=True)
    def state_area(self, region_id, mode, **kw):
        _logger.info("state_area")
        _logger.info(region_id)
        district=request.env['state.region2'].search([('region1','=',region_id.id)])
        area=[(st.id, st.name, st.region1) for st in district]
        _logger.info(area)
        return dict(
             
            district=area,
             
        )
    @http.route(['/shop/state_district/<model("state.region"):district>'], type='json', auth="public", methods=['POST'], website=True)
    def state_district(self, district, mode, **kw):
        _logger.info("state_area")
        _logger.info(district)
        partition=request.env['state.region'].search([('region2','=',district.id)])
        area=[(st.id, st.name, st.region2) for st in partition]
        _logger.info(area)
        return dict(
             
            partition=area,
             
        )
     

class website_delivery(WebsiteSaleDelivery):
    def _get_shop_payment_values(self, order, **kwargs):
        _logger.info("_get_shop_payment_values  delivery  ******************")

        values = super(WebsiteSaleDelivery, self)._get_shop_payment_values(order, **kwargs)
        has_storable_products = any(line.product_id.type in ['consu', 'product'] for line in order.order_line)

        if not order._get_delivery_methods() and has_storable_products:
            values['errors'].append(
                (_('Sorry, we are unable to ship your order'),
                 _('No shipping method is available for your current order and shipping address. '
                   'Please contact us for more information.')))

        if has_storable_products:
            if order.carrier_id and not order.delivery_rating_success:
                order._remove_delivery_line()

            delivery_carriers = order._get_delivery_methods()
            _logger.info("delivery_carriers")
            _logger.info(delivery_carriers)
            _logger.info(order.partner_id)
            _logger.info(type(delivery_carriers))
            #delivery_carriers=request.env['delivery.carrier'].search([('id','=',4)])
            values['deliveries'] = delivery_carriers.sudo()

        values['delivery_has_storable'] = has_storable_products
        values['delivery_action_id'] = request.env.ref('delivery.action_delivery_carrier_form').id
        return values
class partner((models.Model)):
    _inherit="res.partner"
    floor=fields.Char("Floor")
    block=fields.Char("Block")
    region_id=fields.Many2one('state.region1',string='region1',domain="[('state_id','=',state_id)]")
    district=fields.Many2one('state.region2',string='region2',domain="[('region1','=',region_id)]")
    partition=fields.Many2one('state.region',string='region',domain="[('region2','=',district)]")
    """"@api.constrains("email")
    def create_email(self):
        if self.email:
            user=self.env["res.users"].search([])
            values={}
            values={'name':self.name,'login':self.email,'partner_id':self.id,'sel_groups_1_8_9':8}
            _logger.info("Values")
            _logger.info(values)
            user.create(values)"""
class order(models.Model):
    _inherit='sale.order'
    area=fields.Many2one(related='partner_id.region_id',string='Area',store=True)
    district=fields.Many2one(related='partner_id.district',string='District',store=True)
    partition=fields.Many2one(related='partner_id.partition',string='Partition',store=True)
class account_move(models.Model):
    _inherit='account.move'
    area=fields.Many2one(related='partner_id.region_id',string='Area',store=True)
    district=fields.Many2one(related='partner_id.district',string='District',store=True)
    partition=fields.Many2one(related='partner_id.partition',string='Partition',store=True)