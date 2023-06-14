from odoo import models, fields, api

class BHHrAttendance(models.Model):
    _inherit = 'hr.attendance'

    attendance_location = fields.Many2one('hr.attendance.location', 'Check in location')

    @api.model
    def create(self, values):
        if self.env.context.get('current_location'):
            location_code = self.env.context.get('current_location')
            location_record = self.env['hr.attendance.location'].search([('code', '=', location_code)], limit=1)
            if location_record:
                values['attendance_location'] = location_record.id

        return super(BHHrAttendance, self).create(values)
