from odoo import models, fields, api


class PharmacyDashboard(models.Model):
    _name = "pharmacy.dashboard"
    _description = "Pharmacy Dashboard"

    name = fields.Char(default="Dashboard")

    total_medicines = fields.Integer(compute="_compute_data")
    total_customers = fields.Integer(compute="_compute_data")
    total_sales = fields.Integer(compute="_compute_data")
    total_revenue = fields.Float(compute="_compute_data")

    @api.model
    def open_dashboard(self):
        dashboard = self.search([], limit=1)
        if not dashboard:
            dashboard = self.create({})
        return {
            "type": "ir.actions.act_window",
            "res_model": "pharmacy.dashboard",
            "res_id": dashboard.id,
            "view_mode": "form",
            "target": "current",
        }

    @api.depends("name")
    def _compute_data(self):
        for rec in self:
            rec.total_medicines = self.env["pharmacy.medicine"].search_count([])
            rec.total_customers = self.env["pharmacy.customer"].search_count([])
            rec.total_sales = self.env["pharmacy.sale"].search_count([])
            rec.total_revenue = sum(
                self.env["pharmacy.sale"]
                .search([("state", "=", "confirmed")])
                .mapped("total_amount")
            )