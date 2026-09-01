from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livre'

    name = fields.Char(required=True)
    borrower_id = fields.Many2one('res.partner', string='Emprunteur')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('available', 'Disponible'),
        ('borrowed', 'Emprunté'),
    ], default='draft')
    due_date = fields.Date()
    is_overdue = fields.Boolean(compute='_compute_is_overdue', store=True)

    @api.depends('due_date')
    def _compute_is_overdue(self):
        for rec in self:
            rec.is_overdue = bool(rec.due_date and rec.due_date < fields.Date.today())

    @api.constrains('state', 'borrower_id')
    def _check_borrower_required(self):
        for rec in self:
            if rec.state == 'borrowed' and not rec.borrower_id:
                raise ValidationError("Un emprunteur est requis pour marquer un livre comme emprunté.")

    def action_set_available(self):
        for rec in self:
            rec.write({'state': 'available', 'borrower_id': False, 'due_date': False})

    def action_set_borrowed(self):
        for rec in self:
            if not rec.borrower_id:
                raise UserError("Sélectionne un emprunteur avant de marquer ce livre comme emprunté.")
            rec.write({
                'state': 'borrowed',
                'due_date': fields.Date.today() + timedelta(days=14),
            })
            