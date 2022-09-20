from odoo import api, fields, models, _
from odoo.exceptions import UserError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    name = fields.Char('Order Reference', required=True, readonly=True, default="New")
    prescription = fields.Text('Prescription')
    medicine_line = fields.One2many('appointment.medicine.lines', 'appointment_id', string='Medicine Lines')
    note = fields.Text('Description', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')], default='draft', string="Status")
    date_appointment = fields.Date('Date Appointment')
    age = fields.Integer('Age', related='patient_id.age')
    date_checkup = fields.Date('Checkup Time')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        res = super(HospitalAppointment, self).create(vals)
        return res

    def copy(self, default=None):
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = _("%s (Copy)") % self.name
        return super(HospitalAppointment, self).copy(default=default)

    def unlink(self):
        for i in self:
            if i.state != 'draft':
                raise UserError(_('Just can delete appointment in status draft'))
        return super().unlink()

    @api.model
    def default_get(self, fields):
        vals = super(HospitalAppointment, self).default_get(fields)
        vals['note'] = "Patient note"
        return vals
        
    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.gender = self.patient_id.gender
        
        
    def action_draft(self):
        self.write ({'state' : 'draft'})

    def action_confirm(self):
        self.write ({'state' : 'confirm'})

    def action_cancel(self):
        self.write ({'state' : 'cancel'})

    def action_done(self):
        self.write ({'state' : 'done'})

class AppointmentMedicineLines(models.Model):
    _name = 'appointment.medicine.lines'
    _description = 'Appointment Medicine Lines'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    name = fields.Char('Name')
    qty = fields.Integer('Quantity')
