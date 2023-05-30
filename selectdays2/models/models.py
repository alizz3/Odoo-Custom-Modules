from odoo import models, fields
from datetime import timedelta


class BaseModelExtension(models.AbstractModel):
    _inherit = 'base'

    dias_pago = fields.Selection([
        ('30', '30 días'),
        ('45', '45 días'),
        ('90', '90 días'),
        ('other', 'Otro'),
    ], string='Plazo de Pago', default='30')


    otros_dias_pago = fields.Integer(
        string='Otros Plazo de Pago'
    )

    Fecha_limite_pago = fields.Date(
        string='Fecha Límite de Pago',
        compute='_compute_fecha_vencimiento',
    )


    def _compute_fecha_vencimiento(self):
        for solicitud in self:
            if solicitud.dias_pago:
                if solicitud.dias_pago == 'other' and solicitud.otros_dias_pago and solicitud.otros_dias_pago > 0:
                    dias = solicitud.otros_dias_pago
                else:
                    dias = int(solicitud.dias_pago) if solicitud.dias_pago.isdigit() else 0
                    
                if dias > 0:
                    solicitud.Fecha_limite_pago = solicitud.create_date + timedelta(days=dias)
                else:
                    solicitud.Fecha_limite_pago = solicitud.create_date
            else:
                solicitud.Fecha_limite_pago = False



"""
Módulo para cálculo de fecha límite de pago en Odoo.

Este módulo define la clase `BaseModelExtension`, la cual extiende el modelo base en Odoo para agregar funcionalidad relacionada con el cálculo de la fecha límite de pago.

La clase `BaseModelExtension` hereda de la clase `models.AbstractModel` y se utiliza como base para otros modelos en el sistema.

Atributos:
- `dias_pago`: Campo de selección que representa el plazo de pago. Las opciones disponibles son 90 días, 45 días, 30 días y Otro.
- `otros_dias_pago`: Campo entero utilizado cuando se selecciona la opción "Otro" en el campo `dias_pago`. Permite especificar un valor personalizado para el plazo de pago.
- `Fecha_limite_pago`: Campo de tipo `Date` que almacena la fecha límite de pago calculada en función del plazo de pago seleccionado y la fecha de creación.

Métodos:
- `_compute_fecha_vencimiento`: Método de cálculo de la fecha límite de pago. Se ejecuta cada vez que se actualiza alguno de los campos relevantes en el modelo. Calcula la fecha límite de pago en función del plazo de pago seleccionado y la fecha de creación. Si no se selecciona ningún plazo de pago, se establece la fecha límite de pago como False.

Uso:
Este módulo debe ser instalado y configurado en el entorno de Odoo para habilitar el cálculo de la fecha límite de pago en los modelos que heredan de `BaseModelExtension`. Se recomienda utilizar este módulo en aquellos modelos que requieran funcionalidad relacionada con los plazos de pago y el seguimiento de fechas límite de pago.

Nota: Asegúrate de que el modelo en el que se utiliza la clase `BaseModelExtension` tenga un campo `create_date` que represente la fecha de creación. Este campo es necesario para el cálculo correcto de la fecha límite de pago.
"""

