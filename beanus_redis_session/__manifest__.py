# -*- coding: utf-8 -*-
{
    'name': "Utilities: Redis Session Storage",

    'summary': """
       This module is used to change the way odoo store the user session. The Session will be store in Redis Database.""",

    'description': """
        This module is used to change the way odoo store the user session. 
        The Session will be store in Redis Database instead of local file system.
    """,

    'author': "The Bean Family",
    'license': "LGPL-3",
    'website': "https://thebeanfamily.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Bean Family Modules/Utilities',
    'version': '1.0.0',


    # any module necessary for this one to work correctly
    'depends': ['base'],
}
