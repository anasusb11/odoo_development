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

    def unlink(self):
        for i in self:
            if i.state != 'draft':
                raise UserError(_('Transaksi hanya bisa dihapus pada state Draft'))
        return super().unlink()