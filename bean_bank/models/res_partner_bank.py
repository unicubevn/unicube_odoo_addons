#  Copyright (c) by The Bean Family, 2023.
#
#  License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#  These code are maintained by The Bean Family.
import json
from email.policy import default
from odoo import models, fields, api, _

""" Customize the res_partner_bank model
    - Add @static_qr to store the Napas static account QR string
    - Add compute function for @acc_holder_name to get partner name when the @partner_id is change
    - Add compute function for @currency_id to get the default currency_id of current Company
    - Customize the name_get function to show bank account name as 'acc_number-acc_bank_name-acc_holder_name'
"""

class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"
    
    
    acc_object = fields.Char ("Bank Account Object", compute="_make_acc_obj",store=True)
    acc_holder_name = fields.Char(string='Account Holder Name', help="Account holder name, in case it is different than the name of the Account Holder",
                                  compute="_add_partner_name",store=True,readonly=False)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    def name_get(self):
        res = []
        for item in self:
            name = "%s-%s-%s" % (item.acc_number,item.bank_id.name,item.acc_holder_name if (item.acc_holder_name!=False) else "No name")
            res.append((item.id,name))
           
        return res
    
    @api.depends('acc_number','bank_bic')
    def _make_acc_obj(self):
        for acc in self:
            if acc.acc_number != False:
                is_bank_acc = True
                if "9704" in acc.acc_number:
                    is_bank_acc = False
                acc.acc_object = json.dumps(dict(
                    is_bank_account= is_bank_acc,
                    acc_number=acc.acc_number,
                    acc_holder_name=acc.acc_holder_name,
                    bank_code=acc.bank_id.bic,
                    bank_code_name=acc.bank_id.name,
                    bank_name=acc.bank_id.full_name,
                ))

            else:
                acc.acc_object = False
            
    @api.depends('partner_id')
    def _add_partner_name(self):
        print("self.env.company.currency_id",self.env.company.currency_id)
        for acc in self:
            if acc.partner_id != False:
                acc.acc_holder_name = acc.partner_id.name
            
    """_This section is Override the original 'retrieve_acc_type' function_
        Logic:
            - Check if '9704' is exist in acc_number , that is an ATM card account
            - Otherwise, that is a bank account
    """
    @api.model
    def retrieve_acc_type(self, acc_number):
        """ To be overridden by subclasses in order to support other account_types.
        """
        if  acc_number == False or "9704" not in acc_number:
            return 'bank'
        else:
            return 'atm'
        
    """_This section is Override the original '_get_supported_account_types' function_
       -  The original Odoo only support 'bank' type
       -  We add more custome bank type or e-wallet account type here
    """
    @api.model
    def _get_supported_account_types(self):
        return [('bank', _('Bank account')),
                ('atm', _('ATM card'))]
            
        