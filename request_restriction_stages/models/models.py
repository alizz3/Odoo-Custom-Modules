from odoo.exceptions import UserError
from odoo import models, api


class limitandoEtapas(models.AbstractModel):
    _inherit = 'base'  # Nombre del modelo a heredar

    @api.model
    def write(self, values):
        if self._name == 'x_solicitudes_2_0' and 'x_studio_stage_id' in values and values['x_studio_stage_id'] in [1, 2, 3, 4, 5, 8, 6] and (self.x_studio_requerimiento_1 == 'Despachar & Facturar' or self.x_studio_requerimiento_1 == 'Facturar'):
            if (self.env.user.id == 6 or self.env.user.id == 7) and ('x_studio_stage_id' in values and values['x_studio_stage_id'] in [8, 6]):
                raise UserError(
                    'No tienes permiso para pasar a la etapa Cartera Pendiente o Cierre, para las solicitudes con requerimiento "Despachar & Facturar" o "Facturar".')
            elif self.x_studio_factura == False and self.x_studio_selection_field_Gxiuf != "Factura Cancelada" and 'x_studio_stage_id' in values and values['x_studio_stage_id'] in [8, 6]:
                raise UserError(
                    'No puedes pasar a la etapa de cierre porque la solicitud requiere un número de factura establecido.')
        return super(limitandoEtapas, self).write(values)



"""
Sobrescribe el método 'write' del modelo base para aplicar limitaciones en las etapas de las solicitudes.

param values: Diccionario con los valores a escribir en los registros.
return: Superclase del método 'write' para continuar con el comportamiento predeterminado.
raise UserError: Excepción lanzada cuando se violan las restricciones de las etapas.

Restricciones:
- Si el modelo es 'x_solicitudes_2_0' y se cambia el campo 'x_studio_stage_id' a una de las siguientes etapas:
    [Nueva Solicitud, Sin Stock, Preparado, Despachado, Facturar, Cartera Pendiente, Cierre] y el campo 'x_studio_requerimiento_1' es igual a 'Despachar & Facturar' o 'Facturar', solo los usuarios con ID 6 o 7 no pueden pasar a las etapas 'Cartera Pendiente' o 'Cierre'.
- Si el campo 'factura' no ets establecido y el campo 'estado' no es igual a "Factura Cancelada",
    y se intenta cambiar el campo 'etapa' a las etapas [Cartera Pendiente, Cierre], se lanza una excepción indicando que se requiere un número de factura establecido para pasar a la etapa de cierre.

"""

