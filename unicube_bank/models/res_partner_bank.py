#  Copyright (c) by The Bean Family, 2023.
#
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#  These code are maintained by The Bean Family.
import json
from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

""" Customize the res_partner_bank model
    - Add @static_qr to store the Napas static account QR string
    - Add compute function for @acc_holder_name to get partner name when the @partner_id is change
    - Customize the name_get function to show bank account name as 'acc_number-acc_bank_name-acc_holder_name'
"""


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    acc_object = fields.Char("Bank Account Object", compute="_make_acc_obj", store=True)

    def name_get(self):
        res = []
        for item in self:
            name = "%s-%s-%s" % (
            item.acc_number, item.bank_id.name, item.acc_holder_name if (not item.acc_holder_name) else "No name")
            res.append((item.id, name))

        return res

    def get_qr_data(self,qr_method, amount, currency, debtor_partner, free_communication, structured_communication):
        return self._get_qr_code_url(qr_method, amount, currency, debtor_partner, free_communication, structured_communication)
    @api.depends('acc_number', 'bank_bic')
    def _make_acc_obj(self):
        for acc in self:
            if acc.acc_number:
                acc.acc_object = json.dumps(dict(
                    is_bank_account=(not ("9704" in acc.acc_number)),
                    acc_number=acc.acc_number,
                    acc_holder_name= acc.acc_holder_name,
                    bank_code=acc.bank_id.bic,
                    bank_code_name=acc.bank_id.name,
                    bank_name=acc.bank_id.full_name,
                ))
            else:
                acc.acc_object = False
            print(f"acc.proxy_type {acc.proxy_type}")
            if not acc.proxy_type:
                acc.proxy_type = "bank_acc" if (not acc.acc_number or "9704" not in acc.acc_number) else "atm_card"
                acc.proxy_value = acc.acc_number

                    # @api.depends('partner_id')
    # def _add_partner_name(self):
    #     for acc in self:
    #         print(f"acc.partner_id{ acc.partner_id}")
    #         if acc.partner_id:
    #             acc.acc_holder_name = acc.partner_id.name

    """_This section is Override the original 'retrieve_acc_type' function_
        Logic:
            - Check if '9704' is exist in acc_number , that is an ATM card account
            - Otherwise, that is a bank account
    """
    @api.model
    def retrieve_acc_type(self, acc_number):
        try:
            return 'bank' if (not acc_number or "9704" not in acc_number) else 'atm_card'
        except Exception as e :
            return super(ResPartnerBank, self).retrieve_acc_type(acc_number)





    """_This section is Override the original '_get_supported_account_types' function_
       -  The original Odoo only support 'bank' type
       -  We add more custom bank type or e-wallet account type here
    """
    @api.model
    def _get_supported_account_types(self):
        rslt = super(ResPartnerBank, self)._get_supported_account_types()
        rslt.append(('atm_card', _('ATM card')))
        return rslt

