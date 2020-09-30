from odoo import api, fields, models


class PeriodicalReportProduct(models.TransientModel):
    _name = "competitors.data"

    creation_date = fields.Date(string='creation data')

    competitor_id = fields.Many2many('res.competitor', string='Competitor')

    def check_report(self):
        list = []
        for rec in self.competitor_id:
            list.append(rec.id)
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'creation_date':self.creation_date,
                'competitor_id': list

            },
        }
        return self.env.ref('competitor_user.action_competitor_report').report_action(self, data=data)
