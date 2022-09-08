from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.product'
    _description = "Product özelleştirmeleri"
    gtipno = fields.Char('GTİP No')

    def action_gtip_no_linki(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'https://uygulama.gtb.gov.tr/Tara',
                'target': 'new',
            }
