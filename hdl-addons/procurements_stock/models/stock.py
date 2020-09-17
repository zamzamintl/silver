from collections import namedtuple, OrderedDict, defaultdict
from dateutil.relativedelta import relativedelta
from odoo.tools.misc import split_every
from psycopg2 import OperationalError

from odoo import api, fields, models, registry, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare, float_is_zero, float_round

from odoo.exceptions import UserError


class stock(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def _run_scheduler_tasks(self, use_new_cursor=False, company_id=False):
        # Minimum stock rules
        self.sudo()._procure_orderpoint_confirm(use_new_cursor=use_new_cursor, company_id=company_id)

        # Search all confirmed stock_moves and try to assign them
        domain = self._get_moves_to_assign_domain()
        moves_to_assign = self.env['stock.move'].search(domain, limit=None,
                                                        order='priority desc, date_expected asc')
        # for moves_chunk in split_every(100, moves_to_assign.ids):
        #     self.env['stock.move'].browse(moves_chunk)._action_assign()
        #     if use_new_cursor:
        #         self._cr.commit()

        if use_new_cursor:
            self._cr.commit()

        # Merge duplicated quants
        self.env['stock.quant']._quant_tasks()
        if use_new_cursor:
            self._cr.commit()