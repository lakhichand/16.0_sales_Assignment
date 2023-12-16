from odoo import models, fields

class DeliveryCustomization(models.Model):
    _name = 'delivery.customization'
    _description = 'Delivery Customization'

    availble = fields.Boolean(string='Available')
    max_shipping_day = fields.Integer(string='Max Shipping Day')
    