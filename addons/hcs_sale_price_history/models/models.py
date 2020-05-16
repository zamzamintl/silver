# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    item_limit = fields.Integer('Item Limit')
    price_history_based = fields.Selection([
        ('order_confirm', 'order confirm'),
        ('done_one', 'Done (Locked)'),
        ('both', 'Both')],
        default='both', string="Price History Based On")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('hcs_sale_price_history.price_history_based',
                                                         self.price_history_based)
        self.env['ir.config_parameter'].sudo().set_param('hcs_sale_price_history.item_limit', self.item_limit)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            price_history_based=self.env['ir.config_parameter'].sudo().get_param(
                'hcs_sale_price_history.price_history_based'),
            item_limit=int(
                self.env['ir.config_parameter'].sudo().get_param('hcs_sale_price_history.item_limit'))
        )
        return res


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    attribute_sales_ids = fields.One2many('sale.order.line', "product_tmpl_id", string="Sale Price History",
                                          compute='_compute_sale_history')

    @api.depends('attribute_sales_ids.product_tmpl_id')
    def _compute_sale_history(self):
        params = self.env['ir.config_parameter'].sudo()
        for product_template in self:
            product_id = self.env['product.product'].search([('product_tmpl_id', '=', product_template.id)])
            lines = self.env['sale.order.line']
            if params.get_param('hcs_sale_price_history.item_limit') and params.get_param(
                    'hcs_sale_price_history.price_history_based'):
                lines = self.env['sale.order.line'].search([('product_id', '=', product_id.id)], limit=int(
                    params.get_param('hcs_sale_price_history.item_limit')))
                if params.get_param('hcs_sale_price_history.price_history_based') == 'order_confirm':
                    lines.filtered(lambda l: l.state == 'sale')
                elif params.get_param('hcs_sale_price_history.price_history_based') == 'done_one':
                    lines.filtered(lambda l: l.state == 'done')
                else:
                    lines.filtered(lambda l: l.state in ['sale', 'done'])
            if lines:
                product_template.attribute_sales_ids = [(6, 0, lines.ids)]
            else:
                product_template.attribute_sales_ids = [(4, False)]


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_tmpl_id = fields.Many2one('product.template', compute='_compute_parent_values')
    partner_id = fields.Many2one('res.partner', compute='_compute_parent_values')
    user_id = fields.Many2one('res.users', compute='_compute_parent_values')
    date_order = fields.Datetime(compute='_compute_parent_values')

    @api.depends('partner_id')
    def _compute_parent_values(self):
        for record in self:
            record.partner_id = record.order_id.partner_id.id
            record.product_tmpl_id = record.product_id.product_tmpl_id.id
            record.user_id = record.order_id.user_id.id
            record.date_order = record.order_id.date_order
