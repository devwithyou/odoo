from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student"

    admission_no = fields.Char(required=True)
    admission_date = fields.Date(required=True)

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)

    name = fields.Char(
        compute="_compute_name",
        store=True
    )

    email = fields.Char()
    phone = fields.Char(required=True)
    address = fields.Char()

    country_id = fields.Many2one('res.country')

    class_id = fields.Many2one(
        'school.class',
        string="Class"
    )

    father_name = fields.Char()
    mother_name = fields.Char()

    remarks_ids = fields.One2many(
        'school.student.remarks',
        'student_id',
        string="Remarks"
    )

    attendance_ids = fields.One2many(
        'school.attendance',
        'student_id',
        string="Attendance"
    )

    attendance_count = fields.Integer(
        string="Attendance Count",
        compute="_compute_attendance_count"
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='draft')

    _sql_constraints = [
        (
            'unique_admission_no',
            'unique(admission_no)',
            'Admission must be unique!'
        )
    ]

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()

    @api.depends('attendance_ids')
    def _compute_attendance_count(self):
        for rec in self:
            rec.attendance_count = len(rec.attendance_ids)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'