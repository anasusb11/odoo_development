# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': "Hospital Management Software",

    'description': """
        Hospital Management Software by Odoo Mates
    """,

    'author': "Odoo Mates",
    'website': "http://www.odoomates.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': [
        'data/data_sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/appointment.xml',
        'views/menuitems.xml',
    ],
    # only loaded in demonstration mode

    # add module in apps list
    'installable': True,
    'auto_install': False,
    'application': True, 
}
