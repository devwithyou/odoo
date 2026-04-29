from odoo import models, fields

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher"

    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()