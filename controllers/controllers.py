# -*- coding: utf-8 -*-
from odoo import http

# class MiMusica(http.Controller):
#     @http.route('/mi_musica/mi_musica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_musica/mi_musica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_musica.listing', {
#             'root': '/mi_musica/mi_musica',
#             'objects': http.request.env['mi_musica.mi_musica'].search([]),
#         })

#     @http.route('/mi_musica/mi_musica/objects/<model("mi_musica.mi_musica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_musica.object', {
#             'object': obj
#         })