from odoo import models, fields, api
from num2words import num2words

class PurchaseOrder(models.Model):
    _inherit='purchase.order'
    
    
    amount_in_words = fields.Char(string='Amount in Words', compute='amount_to_words') 
        
    @api.depends('amount_total')
    def amount_to_words(self):
        for order in self:
            
            if order.env.user.lang == 'fr_FR':
                user_lang =  'fr'
            else :
                user_lang =  'en'
            
            currency_unit = order.currency_id.currency_unit_label
            currency_subunit = order.currency_id.currency_subunit_label
            dirhams, centimes = divmod(order.amount_total, 1)
            dirhams_words = num2words(int(dirhams), lang=user_lang)
            centimes_words = ''
            if centimes > 0:
                if user_lang =='fr':
                    centimes_words = f"et {num2words(int(centimes*100 + 0.5), lang=user_lang)} {currency_subunit}"
                else :
                    centimes_words = f"and {num2words(int(centimes*100 + 0.5), lang=user_lang)} {currency_subunit}"
                    
            order.amount_in_words = f"{dirhams_words} {currency_unit} {centimes_words}"   
   