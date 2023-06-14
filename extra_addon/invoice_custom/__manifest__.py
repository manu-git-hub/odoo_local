# -*- coding: utf-8 -*-
{
    'name': "invoice_custom",

    'summary': """
       Add a button to convert an invoice docx file to pdf""",

    'description': """
        This module adds a new button to the invoice form view, which allows you to convert a docx file to pdf and attach it to the invoice.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Invoicing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/invoice_form.xml',

    ],

}
