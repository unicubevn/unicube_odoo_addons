import json

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    qr_raw_data = fields.Char(string="QR data", compute="_compute_qr_data", store=True)

    @api.depends('partner_bank_id','amount_residual')
    def _compute_qr_data(self):
        # if self.state != 'draft':
            print("Compute funciton run")
            bank_acc = json.loads(self.partner_bank_id.acc_object)
            print(f"bank_acc: type:{type(bank_acc)} -  {bank_acc}")
            # get_qr_data(self,qr_method, amount, currency, debtor_partner, free_communication, structured_communication):
            qr_data = self.partner_bank_id.get_qr_data('emv_qr', self.amount_residual, self.currency_id, '', '',
                                                       f"Paybill {self.name}")

            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            print(f"qr_data: {base_url}{qr_data}")
            print(f"state: {self.state}")

            self.qr_raw_data = f"{qr_data}"
        # else:
        #     self.qr_raw_data = False

