# -*- coding: utf-8 -*-
{
    'name': "Product price adjust to round good-looking value with included taxes,\
    works only with taxes, not included in the price, finally creating good-looking displayed amount...",
    'author': "QArea, Yury Stasovsky",
    'license': 'LGPL-3',
    'website' : "https://qarea.us",
    'category': 'Custom integration',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/product_product.xml',
            ],
    'installable': True,
}
