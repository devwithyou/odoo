from odoo import models, fields, api


class PharmacyMedicine(models.Model):
    _name = "pharmacy.medicine"
    _description = "Medicine"

    name = fields.Char(required=True)
    default_code = fields.Char(string="Internal Reference")
    manufacturer = fields.Char()

    sale_price = fields.Float(string="Sale Price")
    cost_price = fields.Float(string="Cost")

    active = fields.Boolean(default=True)

    batch_ids = fields.One2many("pharmacy.batch", "medicine_id", string="Batches")
    available_qty = fields.Float(string="Available Qty", compute="_compute_available_qty")

    _sql_constraints = [
        ("unique_default_code", "unique(default_code)", "Internal Reference must be unique!"),
    ]

    @api.depends("batch_ids.quantity", "batch_ids.active")
    def _compute_available_qty(self):
        for rec in self:
            rec.available_qty = sum(rec.batch_ids.filtered(lambda b: b.active).mapped("quantity"))

