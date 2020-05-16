# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


@api.model
def _lang_get(self):
    return self.env['res.lang'].get_installed()


class ResPartnerCaregory(models.Model):
    _name = "res.partner.cat"

    name = fields.Char('name', required=True)
    type = fields.Selection(string="Type", selection=[('dist', 'distributor'),
                                                      ('partner', 'Partner'), ],
                            required=False, )

    def partner_view(self):
        self.ensure_one()
        domain = [
            ('cat_id', '=', self.id)]
        return {
            'name': _('Customers'),
            'domain': domain,
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'help': _('''<p class="oe_view_nocontent_create">
                               Click to Create for Customers
                            </p>'''),
            'limit': 80,

        }


class ResPartner(models.Model):
    _inherit = "res.partner"

    cat_id = fields.Many2one(comodel_name='res.partner.cat',
                             string='Category', )
