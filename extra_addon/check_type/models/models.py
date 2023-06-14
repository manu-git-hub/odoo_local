from odoo import api, fields, models

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.onchange('attendance_location')
    def _onchange_attendance_location(self):
        if self.attendance_location.code == 'HOME':
            self.employee_id.attendance_status = 'Home'
        elif self.attendance_location.code == 'COMP':
            self.employee_id.attendance_status = 'Company'

class Employee(models.Model):
    _inherit = 'hr.employee'

    attendance_ids = fields.One2many('hr.attendance', 'employee_id', string='Attendance Records')
    attendance_status = fields.Selection([
        ('Home', 'Home'),
        ('Company', 'Company'),
        ('Offline', 'Offline'),  
    ], compute='_compute_attendance_status', string='Attendance Status', store=True)


    @api.depends('attendance_ids.attendance_location', 'attendance_ids.check_out')
    def _compute_attendance_status(self):
        for employee in self:
            check_in_count = 0
            check_out_count = 0
            for attendance in employee.attendance_ids:
                if attendance.check_in:
                    check_in_count += 1
                if attendance.check_out:
                    check_out_count += 1
            if check_in_count > check_out_count:
                attendance_location = employee.attendance_ids.filtered(lambda r: r.attendance_location).sorted('create_date', reverse=True)
                if attendance_location and attendance_location[0].attendance_location.code == 'HOME':
                    employee.attendance_status = 'Home'
                elif attendance_location and attendance_location[0].attendance_location.code == 'COMP':
                    employee.attendance_status = 'Company'
                elif not any(attendance.check_in for attendance in employee.attendance_ids) and any(attendance.check_out for attendance in employee.attendance_ids):
                    employee.attendance_status = 'Offline' 
            else:
                employee.attendance_status = 'Offline'