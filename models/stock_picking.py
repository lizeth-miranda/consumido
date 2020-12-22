# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class Consumido(models.Model):
    _inherit = 'stock.picking'

    orden_fab = fields.Many2one(
        'mrp.production', 'Orden de Producción',
        index=True,
    )

    total = fields.Float(
        related='orden_fab.total_consumido'
    )

    unidad_medida = fields.Char(
        string="Unidad de Medida",
        related='orden_fab.move_raw_ids.product_uom.name'
    )
