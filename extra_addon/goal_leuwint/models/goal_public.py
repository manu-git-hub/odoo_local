from odoo import models, fields

class HrEmployeePublicExtended(models.Model):
    _inherit = 'hr.employee.public'

    company_goal = fields.Char(string='Company Goal')
    employee_goal = fields.Char(string='Employee Goal')
