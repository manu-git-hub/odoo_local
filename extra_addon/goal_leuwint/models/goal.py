from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    company_goal = fields.Char(string='Company Goal', store=True,
                               groups=[])
    employee_goal = fields.Char(string='Employee Goal', store=True,
                                groups=[])