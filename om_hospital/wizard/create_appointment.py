from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char('Name', required=True, default="New")
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        self.ensure_one()
        pass
    