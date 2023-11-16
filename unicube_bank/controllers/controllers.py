# -*- coding: utf-8 -*-
# from odoo import http


# class BeanBank(http.Controller):
#     @http.route('/unicube_bank/unicube_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unicube_bank/unicube_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('unicube_bank.listing', {
#             'root': '/unicube_bank/unicube_bank',
#             'objects': http.request.env['unicube_bank.unicube_bank'].search([]),
#         })

#     @http.route('/unicube_bank/unicube_bank/objects/<model("unicube_bank.unicube_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unicube_bank.object', {
#             'object': obj
#         })
