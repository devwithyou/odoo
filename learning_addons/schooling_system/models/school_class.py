from odoo import models, fields

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "School Class"

    name = fields.Char(string="Class Name", required=True)
    section = fields.Char(string="Section")