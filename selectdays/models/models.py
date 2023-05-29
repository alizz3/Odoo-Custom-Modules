from odoo import models, fields
from datetime import timedelta


class BaseModelExtension(models.AbstractModel):
    _inherit = 'base'

    dias_pago = fields.Selection([
        ('90', '90 días'),
        ('45', '45 días'),
        ('30', '30 días'),
        ('2', '2 días'),
    ], string='Plazos de Pago')

    Fecha_limite_pago = fields.Date(
        string='Fecha Limite de Pago',
        compute='_compute_fecha_vencimiento',
    )

    def _compute_fecha_vencimiento(self):
        for solicitud in self:
            if solicitud.dias_pago:
                dias = int(solicitud.dias_pago)
                solicitud.Fecha_limite_pago = solicitud.create_date + timedelta(days=dias)
            else:
                solicitud.Fecha_limite_pago = False


# Esta es la documentación del código proporcionado, que incluye información sobre su funcionalidad y otros detalles relevantes:

# La clase BaseModelExtension hereda de la clase models.AbstractModel en Odoo.
# El atributo _inherit se establece en 'base', lo que indica que esta clase extiende el modelo base en Odoo.
# El campo dias_pago es un campo de selección que representa el plazo de pago. Las opciones disponibles son 90 días, 45 días, 30 días y 2 días.
# El campo Fecha_limite_pago es un campo de tipo Date que representa la fecha límite de pago. Su valor se calcula mediante el método _compute_fecha_vencimiento.
# El método _compute_fecha_vencimiento realiza el cálculo de la fecha límite de pago en función del plazo de pago seleccionado y la fecha de creación. Utiliza la función timedelta del módulo datetime para agregar los días del plazo de pago a la fecha de creación. Si no se selecciona ningún plazo de pago, se establece Fecha_limite_pago como False.
# Este código asume que el modelo en el que se está utilizando la clase BaseModelExtension tiene un campo create_date que representa la fecha de creación. Es necesario que este campo esté presente en la vista para que el cálculo de la fecha límite de pago funcione sin errores no importa si este se encuentra invisible.