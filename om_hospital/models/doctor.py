from xml.dom import ValidationErr
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Doctor'
    _rec_name = 'name'

    name = fields.Char('Name', required=True, tracking=True)
    age = fields.Integer('Age', copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    note = fields.Text('Description', tracking=True)
    img_doctor = fields.Binary('Photo Doctor')

    def copy(self, default=None):
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = _("%s (Copy)") % self.name
        return super(HospitalDoctor, self).copy(default=default)

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            doctor = self.env['hospital.doctor'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if doctor:
                raise UserError(_("Name %s already Exists") % rec.name)

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age == 0:
                raise UserError(_("Age can't by zero "))