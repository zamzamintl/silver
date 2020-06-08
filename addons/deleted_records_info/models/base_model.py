# -*- coding: utf-8 -*-
import os
import base64
import pyscreenshot as ImageGrab
from odoo import api, models

# the list of models data which are to be skipped in the deleted records list.
SKIPPEDTABLELIST = ['deleted.records', 'ir.attachment',
                    'mail.followers', 'mail.message', 'mail.mail', 'ir.model.data']


class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    def unlink(self):
        # common unlink method override.
        deleted_recs = self.env['deleted.records']

        ''' If user will delete records from below list than history record will
            created '''


            # Removed screenshot from system after saving in attachment.
            #os.remove("/tmp/screenshot.png")

        return super(BaseModelExtend, self).unlink()
