from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'base'

# 1. Este fragmento de código define un campo llamado 'current_user' que se utiliza para almacenar el primer usuario conectado al momento de crear un nuevo registro en la vista formulario.

    # current_user = fields.Many2one(
    #     'res.users', 'Current User', default=lambda self: self.env.uid)


# 2. Este fragmento de código define un campo llamado 'current_user' que se utiliza para almacenar el usuario conectado al momento de ver un registro ya guardado.

    # current_user = fields.Many2one(
    #     'res.users', 'Current User', compute='_compute_current_user')

    # Este método calculado '_compute_current_user' se utiliza para asignar el valor del campo 'current_user' con el usuario conectado al momento de ver un registro ya guardado.

    # def _compute_current_user(self):
    #     for record in self:
    #         record.current_user = self.env.user.id

"""
Puedes descomentar y utilizar la parte del código que se ajuste a tus necesidades. Si deseas que el campo 'current_user' se llame de manera diferente, puedes modificar el nombre en los fragmentos de código correspondientes.
"""
