from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.product'
    _description = "Product özelleştirmeleri"
    gtipno = fields.Char('GTİP No')
