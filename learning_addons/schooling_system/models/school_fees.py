from odoo import models, fields

class SchoolFees(models.Model):
    _name = "school.fees"
    _description = "Fees"

    student_id = fields.Many2one('school.student', required=True, ondelete="cascade")
    amount = fields.Float(string="Amount")
    date = fields.Date(string="Date")

    status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], default='unpaid', string="Status")