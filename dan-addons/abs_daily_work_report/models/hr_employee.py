# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

import datetime

#Class Extended For Add New Functionality Of Send Email Of Daily Work Report
class Employee(models.Model):
    _inherit = 'hr.employee'

    mail_button = fields.Selection([('send_status_report','Send Daily Stauts Report')], help="Status Report Mail to Manger")

    #Method Is For Computing Email To Click On send_status_report Button
    def send_status_report(self):
        email_subject = "Status Upadte from " + self.name + " on " + str(datetime.date.today())
        email_to = self.parent_id.user_id.partner_id.id
        if email_to:
            analytic_lines = self.env['account.analytic.line'].search([('user_id', '=', self.user_id.id),('date','=',datetime.date.today())])
            if analytic_lines:
                task_unit_amount = 0.00
                task_description = ""
                total_hours = "" 
                for line in analytic_lines:
                    task_description += "* " + line.name + "<br/>"
                    task_unit_amount += (line.unit_amount)
                    if ((task_unit_amount * 60) % 60) <= 9:
                        total_hours = str(int(task_unit_amount)) + " : " + "0" + str(int((task_unit_amount * 60) % 60))                   
                    else:
                        total_hours = str(int(task_unit_amount)) + " : " + str(int((task_unit_amount * 60) % 60))

                status_table = " <font size=""2"">   <p> Hello {3}, </p>    <p> Today’s status update report: </p>    <table style=""width:80%"" border="" 1px solid black""> <tr font=""2""> <th width=""80%""><font size=""2""> Description</font> </th>    <th width=""20%""><font size=""2""> Duration </font> </th>    </tr>    <tr>    <td> <font size=""2""> {0} </font></td>    <td  align=""center""> <font size=""2""> {1} </font> </td>    </tr>     <tr>    <td  align=""right""><font size=""2""> Total </font></td>    <td  align=""center""><font size=""2""> {1} </font> </td>   </table>       <p>Regards,</p>    <p> {2} </p>    </font>".format(task_description, total_hours,self.name, str(self.parent_id.name)) 

                mail={
              'subject'               : email_subject,
              'email_from'            : self.name,
              'recipient_ids'         : [(6, 0, [email_to])],
              'body_html'             : status_table
             }
                mail_create = self.env['mail.mail'].create(mail)
                if mail_create:
                    mail_create.send()
                    return {'type': 'ir.actions.act_window', 
                            'view_type': 'form', 
                            'view_mode': 'form',
                            'res_model': 'hr.employee.wizard', 
                            'target': 'new', 
                            'context':{'default_message':"Status report has been sent."},
                            }
            else:
                raise ValidationError(_('There is no any timesheets available for today.'))
        else:
            raise ValidationError(_('Please, Add Manager.'))


