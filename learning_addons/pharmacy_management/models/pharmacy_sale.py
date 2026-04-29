from odoo import models, fields, api


class PharmacySale(models.Model):
    _name = "pharmacy.sale"
    _description = "Pharmacy Sale"

    name = fields.Char(required=True, default="New")
    date = fields.Date(default=fields.Date.today, required=True)

    customer_id = fields.Many2one("pharmacy.customer", string="Customer")

    line_ids = fields.One2many("pharmacy.sale.line", "sale_id", string="Lines")
    total_amount = fields.Float(string="Total", compute="_compute_total_amount", store=True)

    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled")],
        default="draft",
    )

    _sql_constraints = [
        ("unique_sale_name", "unique(name)", "Sale Reference must be unique!"),
    ]

    @api.depends("line_ids.subtotal")
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(rec.line_ids.mapped("subtotal"))

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancelled"


class PharmacySaleLine(models.Model):
    _name = "pharmacy.sale.line"
    _description = "Pharmacy Sale Line"

    sale_id = fields.Many2one("pharmacy.sale", required=True, ondelete="cascade")

    medicine_id = fields.Many2one("pharmacy.medicine", required=True)
    batch_id = fields.Many2one("pharmacy.batch", string="Batch")

    qty = fields.Float(string="Qty", default=1.0)
    price_unit = fields.Float(string="Unit Price")
    subtotal = fields.Float(compute="_compute_subtotal", store=True)

    @api.depends("qty", "price_unit")
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = (rec.qty or 0.0) * (rec.price_unit or 0.0)

    @api.onchange("medicine_id")
    def _onchange_medicine_id(self):
        if self.medicine_id:
            self.price_unit = self.medicine_id.sale_price
            if self.batch_id and self.batch_id.medicine_id != self.medicine_id:
                self.batch_id = False
            return {
                "domain": {
                    "batch_id": [
                        ("medicine_id", "=", self.medicine_id.id),
                        ("active", "=", True),
                        ("is_expired", "=", False),
                    ]
                }
            }
        self.batch_id = False
        return {"domain": {"batch_id": []}}

