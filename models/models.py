# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeBank(models.Model):
    _inherit = 'res.partner.bank'


    partner_id = fields.Many2one(comodel_name="res.partner", string="", required=False, )


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    certificate = fields.Selection(string="Certificate Level", selection=[('bachelor', 'Bachelor'), ('master', 'Master'), ('hnd', 'HND'), ('ond', 'OND'), ('phd', 'PHD'), ], required=False, )
    guarantor_name = fields.Char(string="Guarantor Name", required=False, )
    guarantor_address = fields.Text(string="Guarantor Address", required=False, )
    guarantor_phone = fields.Char(string="Guarantor Phone", required=False, )
    mobile_phone = fields.Char(string="CUG Mobile", required=False, )
    work_phone = fields.Char(string="Mobile Phone", required=False, )
    coach_id = fields.Many2one(comodel_name="hr.employee", string="Supervisor", required=False, )




# class employeebank(models.Model):
#     _name = 'employeebank.employeebank'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100