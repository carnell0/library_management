from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    borrowed_book_ids = fields.One2many('library.book', 'borrower_id', string='Livres empruntés')
    borrowed_book_count = fields.Integer(compute='_compute_borrowed_book_count')

    def _compute_borrowed_book_count(self):
        for partner in self:
            partner.borrowed_book_count = len(partner.borrowed_book_ids)

    def action_view_borrowed_books(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Livres empruntés',
            'res_model': 'library.book',
            'view_mode': 'list,form',
            'domain': [('borrower_id', '=', self.id)],
        }
        