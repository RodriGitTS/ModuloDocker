# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dam2(models.Model):
    _name = 'dam2.dam2'
    _description = 'dam2.dam2'

    name = fields.Char()
    value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

