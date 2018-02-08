# -*- coding: utf-8 -*-
from openerp import models, fields, api
#from openerp.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class product_product(models.Model):
    _inherit='product.product'
    
    displayed_price = fields.Float(string='Displayed price')
    
    
    
    @api.onchange('displayed_price', 'taxes_id')
    def set_list_price(self):
        for inst in self:
            if not inst.displayed_price:
                continue
            
            TP = inst.displayed_price
            sum_tax = 0
            
            for tax in inst.taxes_id:
                sum_tax += tax.amount/100
                
            PP = TP/(1+sum_tax)
            
            inst.lst_price = PP
                
        
        
            
    