from odoo import api, fields, models

class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    date_appointment = fields.Date('Date Appointment')
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def action_create_appointment(self):
        vals = {

            # create patient from wizard
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
            }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("================================================", appointment_rec)
        return {
                'name': ('Appointment'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'hospital.appointment',
                'res_id': appointment_rec.id
            }
    def action_view_appointment(self):
        # Method 1
        # action = self.env.ref('om_hospital.appointment_action').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # Method 2
        # action = self.env['ir.actions.actions']._for_xml_id('om_hospital.appointment_action')
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # return action

        # Method 3
        return {
                'name': ('Appointment'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'hospital.appointment',
                'target': 'current',
                'domain': [('patient_id', '=', self.patient_id.id)]
            }
        # print("===============================",action)
