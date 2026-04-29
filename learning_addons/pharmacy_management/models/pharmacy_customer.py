from odoo import models, fields


class PharmacyCustomer(models.Model):
    _name = "pharmacy.customer"
    _description = "Customer"

    name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    address = fields.Char()

