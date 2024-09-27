# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloAdrian(http.Controller):
#     @http.route('/modulo_adrian/modulo_adrian', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_adrian/modulo_adrian/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_adrian.listing', {
#             'root': '/modulo_adrian/modulo_adrian',
#             'objects': http.request.env['modulo_adrian.modulo_adrian'].search([]),
#         })

#     @http.route('/modulo_adrian/modulo_adrian/objects/<model("modulo_adrian.modulo_adrian"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_adrian.object', {
#             'object': obj
#         })

