# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

##############################################################################
#
#
#    Copyright (C) 2018-TODAY .
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
##############################################################################

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError,UserError


class Users(models.Model):
    _inherit = "res.users"

    @api.multi
    @api.constrains('groups_id')
    def _check_one_user_type(self):
        res=super(Users, self)._check_one_user_type()
        print('iam on check user type res')

        return res


class Partner(models.Model):
    _inherit = 'res.partner'


    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=False, )
    sec_mail = fields.Char(string="Second Email", required=False,)
    # email = fields.Char(company_dependent=True,)
    # document_ids=fields.One2many(comodel_name='res.partner.document',inverse_name='partner_id',string='Partner Documents')
    doc_cnt=fields.Integer('Documents Count',compute='get_document_count')
    publish_project_cnt=fields.Integer('Publish Project Documents Count',compute='get_publish_project_count')
    related_attachment_cnt = fields.Integer('Related Documents Count', compute='get_related_document_count')

    survey_cnt = fields.Integer('Survey Results Count', compute='get_survey_count')

    @api.multi
    def get_survey_count(self):
        for partner in self:
            partner.survey_cnt = self.env['survey.user_input'].search_count([('partner_id', '=', partner.id)])




    @api.multi
    def get_document_count(self):
        for partner in self:
            partner.doc_cnt=self.env['res.partner.document'].search_count([('partner_id','=',partner.id)])

    @api.multi
    def get_related_document_count(self):
        for partner in self:
            partner.related_attachment_cnt = self.env['ir.attachment'].sudo().search_count(
                [('partner_id', '=', partner.id)])

    @api.multi
    def get_publish_project_count(self):
        for partner in self:
            partner.publish_project_cnt = self.env['ir.attachment'].sudo().search_count(
                [('folder_id.published_projects', '=', True), ('partner_id', '=', partner.id)])


    # @api.constrains('email')
    # def check_mail(self):
    #     print('iam in check mail')
    #     if self.email:
    #         partner_mail_ids = self.search_count([('email', '=', self.email)])
    #         if partner_mail_ids > 1:
    #             raise ValidationError(_('This Email is defined before.'))


    def action_survey_results(self):
        self.ensure_one()
        form_id = self.env.ref("survey.survey_user_input_form")
        tree_id = self.env.ref("survey.survey_user_input_tree")

        domain = []
        doc_ids = self.env['survey.user_input'].sudo().search([('partner_id', '=', self.id)])
        domain += [('id', 'in', doc_ids.ids)]
        context = self._context.copy()
        context['default_partner_id'] = self.id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Survey Results',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'survey.user_input',
            'domain': domain,
            'views': [(tree_id.id, 'tree'), (form_id.id, 'form')],
            'context': context,

            'target': 'current',
        }
    #
    #
    # def action_send_mail(self):
    #     print('i will send mail')

    @api.multi
    def partner_document_action(self):

        form_id = self.env.ref("silver_partner.partner_document_form_view")
        tree_id = self.env.ref("silver_partner.partner_document_tree_view")

        domain = []
        doc_ids = self.env['res.partner.document'].sudo().search([('partner_id', '=', self.id)])
        domain += [('id', 'in', doc_ids.ids)]
        context = self._context.copy()
        context['default_partner_id'] = self.id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Related Documents',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.partner.document',
            'domain': domain,
            'views': [(tree_id.id, 'tree'), (form_id.id, 'form')],
            'context':context,

            'target': 'current',
        }

    @api.multi
    def publish_project_docs(self):

        form_id = self.env.ref("documents.documents_view_form")
        tree_id = self.env.ref("documents.documents_view_list")

        domain = []
        doc_ids = self.env['ir.attachment'].sudo().search([('folder_id.published_projects', '=', True),('partner_id', '=', self.id)])
        domain += [('id', 'in', doc_ids.ids)]
        context = self._context.copy()
        context['default_partner_id'] = self.id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Published Projects Documents',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ir.attachment',
            'domain': domain,
            'views': [(tree_id.id, 'tree'), (form_id.id, 'form')],
            'context': context,

            'target': 'current',
        }

    @api.multi
    def partner_documents(self):

        form_id = self.env.ref("documents.documents_view_form")
        tree_id = self.env.ref("documents.documents_view_list")

        domain = []
        doc_ids = self.env['ir.attachment'].search(
            [('partner_id', '=', self.id)])
        domain += [('id', 'in', doc_ids.ids)]
        context = self._context.copy()
        context['default_partner_id'] = self.id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Published Projects Documents',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'ir.attachment',
            'domain': domain,
            'views': [(tree_id.id, 'tree'), (form_id.id, 'form')],
            'context': context,

            'target': 'current',
        }

class PartnerDocument(models.Model):
    _name="res.partner.document"



    name=fields.Char(string='Name')
    description=fields.Text(string='Description')
    # file=fields.Binary('File',attachment=True)
    doc_attachment_id = fields.Many2many('ir.attachment', 'doc_attach_rel22', 'doc_id22', 'attach_id322', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    partner_id=fields.Many2one(comodel_name='res.partner',string='Partner')
    doc_cnt=fields.Integer('Document Count',compute='get_document_count')

    @api.multi
    @api.depends('doc_attachment_id')
    def get_document_count(self):
        print('iam on the add folder')
        for doc in self:
            print('iam on the add folder')
            if doc.doc_attachment_id:
                doc.doc_attachment_id.write({'folder_id':8})
                doc.doc_cnt=len(doc.doc_attachment_id)
    # file=
