from odoo import models, fields, api

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'

    def create(self, values):
       
        
        self.set_estimated_shipping_date(values)

        return super(SaleOrderLineCustom, self).create(values)