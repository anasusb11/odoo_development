from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    date_appointment = fields.Date('Date Appointment')
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
            }
        self.env['hospital.appointment'].create(vals)
    