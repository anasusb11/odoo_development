from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Doctor'
    _rec_name = 'name'

    name = fields.Char('Name', required=True, tracking=True)
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description', tracking=True)
    img_doctor = fields.Binary('Photo Doctor')
