# -*- coding: utf-8 -*-
{
    'name': "Indoguna-Doc Numbering",

    'summary': """
        Indoguna-Doc Numbering """,

    'description': """
        Indoguna-Doc Numbering
    """,

    'author': "Andy Utomo",
    'website': "http://andyut.blogspot.com",
 
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
        'views/views.xml',
        'menu/menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}