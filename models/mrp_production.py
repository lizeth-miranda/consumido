# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class Consumido(models.Model):
    _inherit = 'mrp.production'

    total_consumido = fields.Float("Total", compute='get_total_consumido')

    def get_total_consumido(self):
        self.total_consumido = round(
            sum(line.quantity_done for line in self.move_raw_ids))
