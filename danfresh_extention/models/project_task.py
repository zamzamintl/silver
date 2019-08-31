# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, datetime, time, timedelta
from odoo.fields import Date, Datetime
from lxml import etree
class Task(models.Model):
    _inherit = 'project.task'


    @api.model
    def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
        # print("LLLLLLLLLLLLLLLLLLLLLLLL", toolbar, submenu)
        res = super(Task, self).fields_view_get(view_id, view_type, toolbar=toolbar, submenu=False)
        group_id = self.env.user.is_kanban_read
        doc = etree.XML(res['arch'])
        if doc:
            if group_id:
                print("_________________")
                if view_type == 'kanban':
                    print(group_id)
                    nodes = doc.xpath("//field[@name='stage_id']")
                    for node in nodes:
                        node.set('readonly', '1')
                        print(node)
                    res['arch'] = etree.tostring(doc)
            if not group_id:
                print(".......................")
                if view_type == 'kanban':
                    nodes = doc.xpath("//field[@name='stage_id']")
                    for node in nodes:
                        node.set('readonly', '')
                    res['arch'] = etree.tostring(doc)

        return res