# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Asset1(models.Model):
    _name = 'asset_management.asset1'
    _description = 'asset_management.asset1'

    name = fields.Char()
    value = fields.Integer(help="just help value")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

