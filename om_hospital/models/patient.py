import imp
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    

    name = fields.Char('Name', required=True)
    age = fields.Char('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description')
