# -*- coding: utf-8 -*-
{
    'name': "check_type",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'author': "Leuwint Technology",
    'website': "https://www.leuwint.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'check_in_location'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
  
        'views/templates.xml',
    ],}
