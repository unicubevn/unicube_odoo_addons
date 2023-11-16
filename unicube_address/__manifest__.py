# -*- coding: utf-8 -*-
{
    'name': "Utilities: Vietnamese Address based on Circular No 124/2004/QĐ-TTg issued by Viet Nam Government (for backend sites only)",

    'summary': """
        This is the Vietnamese address module based on Circular No 124/2004/QĐ-TTg issued by Viet Nam Government (for backend sites only)
            """,

    'description': """
        This is the Vietnamese address module based on Circular No 124/2004/QĐ-TTg issued by Viet Nam Government (for backend sites only)
    """,

    'author': "The Bean Family (an UniCube member)",
    "license": "LGPL-3",
    'website': "https://unicube.vn",
    'category': 'UniCube/Utilities',
    'version': '17.0.0.1',

    "application": True,
    "installable": True,
    "images": ["static/description/image.jpeg"],

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_address_menu.xml',
        'views/res_company_info.xml',
        'data/res.country.state.xml',
        'data/res.country.district.csv',
        'data/res.country.ward.csv'
    ],

}
