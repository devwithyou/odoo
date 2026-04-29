from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = "school.attendance"
    _description = "Student Attendance"
    _rec_name = "student_id"

    student_id = fields.Many2one(
        'school.student',
        string="Student",
        required=True,
        ondelete="cascade"
    )

    date = fields.Date(
        string="Date",
        default=fields.Date.today,
        required=True
    )

    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave')
    ], string="Status", default='present', required=True)

    teacher_id = fields.Many2one(
        'school.teacher',
        string="Marked By"
    )

    _sql_constraints = [
        ('unique_attendance',
         'unique(student_id, date)',
         'Attendance already exists for this student on this date!')
    ]