# -*- coding: utf-8 -*-
from odoo import http

# class /data/iguItDev/cnwNumbering(http.Controller):
#     @http.route('//data/igu_it_dev/cnw_numbering//data/igu_it_dev/cnw_numbering/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//data/igu_it_dev/cnw_numbering//data/igu_it_dev/cnw_numbering/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/data/igu_it_dev/cnw_numbering.listing', {
#             'root': '//data/igu_it_dev/cnw_numbering//data/igu_it_dev/cnw_numbering',
#             'objects': http.request.env['/data/igu_it_dev/cnw_numbering./data/igu_it_dev/cnw_numbering'].search([]),
#         })

#     @http.route('//data/igu_it_dev/cnw_numbering//data/igu_it_dev/cnw_numbering/objects/<model("/data/igu_it_dev/cnw_numbering./data/igu_it_dev/cnw_numbering"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/data/igu_it_dev/cnw_numbering.object', {
#             'object': obj
#         })