from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'name'
    _order = 'name ASC'
        
    partner_id = fields.Many2one('res.partner', string='Partner')
    appointment_line = fields.One2many('hospital.appointment', 'patient_id', string='Appointment Lines')
    name = fields.Char('Name', required=True, tracking=True)
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description', tracking=True)
    ref = fields.Char(default="New", readonly=True, string="Sequence Code")
    active = fields.Boolean('Active')
    appointment_count = fields.Integer(compute='_compute_appointment_count', string='Appointment Count')
    img_patient = fields.Binary('Photo Patient')
    def _compute_appointment_count(self):
        for rec in self:
            # print("============================", rec.id)
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
            self.appointment_count = appointment_count

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        res = super(HospitalPatient, self).create(vals)
        return res