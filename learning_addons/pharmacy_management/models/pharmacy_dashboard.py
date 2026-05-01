from odoo import models, fields, api


class PharmacyDashboard(models.Model):
    _name = "pharmacy.dashboard"
    _description = "Pharmacy Dashboard"

    name = fields.Char(default="Dashboard")

    total_medicines = fields.Integer(compute="_compute_data")
    total_customers = fields.Integer(compute="_compute_data")
    total_sales = fields.Integer(compute="_compute_data")
    total_revenue = fields.Float(compute="_compute_data")

    def _compute_data(self):
        for rec in self:
            rec.total_medicines = self.env["pharmacy.medicine"].search_count([])
            rec.total_customers = self.env["pharmacy.customer"].search_count([])
            rec.total_sales = self.env["pharmacy.sale"].search_count([])

            sales = self.env["pharmacy.sale"].search([("state", "=", "confirmed")])
            rec.total_revenue = sum(sales.mapped("total_amount"))