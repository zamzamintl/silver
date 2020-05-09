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



class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    sec_name=fields.Char(string='Arabic Name')

     
    def name_get(self):
        print('iam on the name get')
        res = []
        for emp in self:
            name = emp.name
            if emp.sec_name:
                name = '%s[%s]' % (emp.name, emp.sec_name)
            res.append((emp.id, name))
        print('iam on the name get',res)
        return res
