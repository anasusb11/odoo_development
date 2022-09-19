from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Doctor'
    

    name = fields.Char('Name', required=True, tracking=True)
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')], default='draft', string="Status")
    ref = fields.Char(default="New", readonly=True, string="Sequence Code")
    img_doctor = fields.Binary('Photo Doctor')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor')
        res = super(HospitalDoctor, self).create(vals)
        return res