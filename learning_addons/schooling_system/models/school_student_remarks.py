from odoo import models, fields

class SchoolStudentRemarks(models.Model):
    _name = "school.student.remarks"
    _description = "Student Remarks"

    student_id = fields.Many2one('school.student', required=True, ondelete="cascade")
    remark = fields.Text(string="Remark")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")
    date = fields.Datetime(default=fields.Datetime.now)