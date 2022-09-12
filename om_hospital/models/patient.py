from email.policy import default
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    

    name = fields.Char('Name', required=True)
    age = fields.Char('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')], default='draft', string="Status")

    def action_draft(self):
        self.write ({'state' : 'draft'})

    def action_confirm(self):
        self.write ({'state' : 'confirm'})

    def action_cancel(self):
        self.write ({'state' : 'cancel'})

    def action_done(self):
        self.write ({'state' : 'done'})