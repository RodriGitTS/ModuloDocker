# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloManuel(http.Controller):
#     @http.route('/modulo_manuel/modulo_manuel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_manuel/modulo_manuel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_manuel.listing', {
#             'root': '/modulo_manuel/modulo_manuel',
#             'objects': http.request.env['modulo_manuel.modulo_manuel'].search([]),
#         })

#     @http.route('/modulo_manuel/modulo_manuel/objects/<model("modulo_manuel.modulo_manuel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_manuel.object', {
#             'object': obj
#         })

