from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    

    partner_id = fields.Many2one('res.partner', string='Partner')
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
    active = fields.Boolean('Active')
    appointment_count = fields.Integer(compute='_compute_appointment_count', string='Appointment Count')
    
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
    def action_draft(self):
        self.write ({'state' : 'draft'})

    def action_confirm(self):
        self.write ({'state' : 'confirm'})

    def action_cancel(self):
        self.write ({'state' : 'cancel'})

    def action_done(self):
        self.write ({'state' : 'done'})