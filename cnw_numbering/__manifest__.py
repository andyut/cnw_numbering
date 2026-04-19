# -*- coding: utf-8 -*-
{
    'name': "AU-Doc Numbering",

    'summary': """
        Manage document numbering by company, month, and year
    """,

    'description': """
        This module provides automatic sequential document numbering
        based on company, suffix, month, and year.
    """,

    'author': "Andy Utomo",
    'website': "http://andyut.blogspot.com",
 
    # for the full list
    'category': 'others',
    'version': '0.1',
    'application':True,
    'images': ['static/description/cover.png'],
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