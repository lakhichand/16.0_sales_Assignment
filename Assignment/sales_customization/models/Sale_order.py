from odoo import models, fields, api

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'

    def create(self, values):
       
        
        self.set_estimated_shipping_date(values)

        return super(SaleOrderLineCustom, self).create(values)

    def set_estimated_shipping_date(self, values):
        
        carrier_id = values.get('order_id') and self.env['sale.order'].browse(values['order_id']).carrier_id.id or self.carrier_id.id
        if carrier_id:
            customisation = self.env['delivery.customisation'].search([('carrier_id', '=', carrier_id)], limit=1)
            if customisation:
                max_shipping_days = customisation.max_shipping_days
                estimated_shipping_date = fields.Datetime.now() + timedelta(days=max_shipping_days)
                values['estimated_shipping_date'] = estimated_shipping_date
    