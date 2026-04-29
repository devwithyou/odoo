from odoo import models, fields, api


class PharmacyBatch(models.Model):
    _name = "pharmacy.batch"
    _description = "Medicine Batch"
    _rec_name = "batch_no"

    batch_no = fields.Char(required=True)
    medicine_id = fields.Many2one("pharmacy.medicine", required=True, ondelete="cascade")

    expiry_date = fields.Date(required=True)
    quantity = fields.Float(default=0.0)

    purchase_price = fields.Float(string="Purchase Price")
    supplier = fields.Char()

    active = fields.Boolean(default=True)
    is_expired = fields.Boolean(string="Expired", compute="_compute_is_expired", store=True)

    _sql_constraints = [
        (
            "unique_batch_per_medicine",
            "unique(medicine_id, batch_no)",
            "Batch No must be unique per Medicine!",
        ),
    ]

    @api.depends("expiry_date")
    def _compute_is_expired(self):
        today = fields.Date.today()
        for rec in self:
            rec.is_expired = bool(rec.expiry_date and rec.expiry_date < today)

