from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livre'

    name = fields.Char(required=True)
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
            