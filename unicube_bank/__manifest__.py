# -*- coding: utf-8 -*-
{
    'name': "Payment: Vietnamese Bank Base Module",

    'summary': """
        This module is the base module for generator VietQR module.(VietQR is the Vietnam's QR standard for payment)""",

    'description': """
        This module is the base module for generator VietQR module. 
        This module will provided:
        -   All the Vietnamese bank info and bankcode which announced by State Bank of Viet Nam.
        -   Add "default bank account" field to res.company model.
        -   Add VietQR for invoice view form.
    """,

    'author': "The Bean Family (an UniCube member)",
    "license": "LGPL-3",
    'category': 'UniCube/Payment',
    'version': '17.0.0.1',
    'website': "https://unicube.vn",
    'support': 'community@thebeanfamily.org',
    "application": True,
    "installable": True,

    "images": ["static/description/image.png"],

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_vn','account_qr_code_emv'],

    # always loaded
    'data': [
        'data/res.bank.csv',
        'views/account_move.xml',
        'views/bank_menu.xml',
        'views/res_bank_account.xml',
        'views/res_company_info.xml',
    ],

}
