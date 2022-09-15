from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    name = fields.Char('Order Reference', required=True, readonly=True, default="New")
    note = fields.Text('Description', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')], default='draft', string="Status")
    date_appointment = fields.Date('Date Appointment')
    age = fields.Integer('Age')
    date_checkup = fields.Date('Checkup Time')
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        res = super(HospitalAppointment, self).create(vals)
        return res
        
    def action_draft(self):
        self.write ({'state' : 'draft'})

    def action_confirm(self):
        self.write ({'state' : 'confirm'})

    def action_cancel(self):
        self.write ({'state' : 'cancel'})

    def action_done(self):
        self.write ({'state' : 'done'})