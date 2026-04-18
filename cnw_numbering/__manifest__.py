# -*- coding: utf-8 -*-
{
    'name': "Indoguna-Doc Numbering",

    'summary': """
        Indoguna-Doc Numbering """,

    'description': """
        Indoguna-Doc Numbering
    """,

    'author': "Indoguna Utama,Andy Utomo",
    'website': "http://www.indoguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'others',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group_users.xml',
        'views/wizard_view.xml',
        'views/views.xml',
        'menu/menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}