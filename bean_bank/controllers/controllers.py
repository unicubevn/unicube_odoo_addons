# -*- coding: utf-8 -*-
# from odoo import http


# class BeanBank(http.Controller):
#     @http.route('/bean_bank/bean_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bean_bank/bean_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bean_bank.listing', {
#             'root': '/bean_bank/bean_bank',
#             'objects': http.request.env['bean_bank.bean_bank'].search([]),
#         })

#     @http.route('/bean_bank/bean_bank/objects/<model("bean_bank.bean_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bean_bank.object', {
#             'object': obj
#         })
