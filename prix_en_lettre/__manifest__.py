# -*- coding: utf-8 -*-
{
    'name': "Prix en lettre Maroc",

    'summary': """
    
        
    """,

    'description': """
       

    """,

    'author': 'D-Business Consulting',
    'company': 'D-Business Consulting',
    'maintainer': 'D-Business Consulting',
    'website': 'https://d-business-consulting.ma',
    'category': 'Sales,Purchases,Accounting',
    'version': '16.0.1.0.0',

    'depends': ['base','account','sale'],

    'data': [
        'reports/invoice.xml',
        'reports/saleorder.xml',
        'reports/purchase.xml',
    ],
    # 'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}