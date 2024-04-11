# -*- coding: utf-8 -*-
{
    'name': "E-Commerce Discount",
    'version': '17.0.1.0.0',
    'depends': ['base', 'product', 'stock', 'sale','website_sale','loyalty'],
    'category': '',
    'description': """
    Discount only apply by orders coming from E-Commerce
    """,
    'data': [
                'data/loyalty_demo.xml',
                'views/res_config_settings_view_form.xml',
             ],
    'demo': [
            'data/loyalty_demo.xml',
        ],
    'application': 'True',
    'installable': True,
}