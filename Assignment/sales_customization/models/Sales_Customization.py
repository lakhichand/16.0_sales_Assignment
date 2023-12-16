from odoo import models, fields, api

class Sales_Customization(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.delivery_shipping_line:
                order.create_delivery_order()
        return res

    def create_delivery_order(self):
        for order in self:
            if order.delivery_shipping_line:
                
                estimated_shipping_date = fields.Date.today() + timedelta(days=order.delivery_shipping_line.delivery_carrier_id.max_shipping_days)

                
                delivery_vals = {
                    'partner_id': order.partner_shipping_id.id,
                    'scheduled_date': estimated_shipping_date,
                    
                }
                delivery_order = self.env['stock.picking'].create(delivery_vals)

                
                for line in order.order_line.filtered(lambda l: l.is_delivery):
                    delivery_line_vals = {
                        'name': line.name,
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.product_uom_qty,
                        'picking_id': delivery_order.id,
                       
                    }
                    self.env['stock.move'].create(delivery_line_vals)
        return True
