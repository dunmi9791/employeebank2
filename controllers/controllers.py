# -*- coding: utf-8 -*-
from odoo import http

# class Employeebank(http.Controller):
#     @http.route('/employeebank/employeebank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employeebank/employeebank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employeebank.listing', {
#             'root': '/employeebank/employeebank',
#             'objects': http.request.env['employeebank.employeebank'].search([]),
#         })

#     @http.route('/employeebank/employeebank/objects/<model("employeebank.employeebank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employeebank.object', {
#             'object': obj
#         })