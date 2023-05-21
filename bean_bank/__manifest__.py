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
    """,

    'author': "The Bean Family",
    "license": "LGPL-3",
    'category': 'Bean Family Modules/Payment',
    'version': '16.0.0.1',
    'website': "https://www.thebeanfamily.org",
    'support': 'community@thebeanfamily.org',
    "application": True,
    "installable": True,

    "images": ["static/description/image.png"],

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/res.bank.csv',
        'views/bank.xml',
        'views/res_bank_account.xml',
        'views/res_company_info.xml',
    ],

}
