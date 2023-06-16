{
    'name': 'Restriction Stages Inventory Movements',
    'version': '1.0',
    'summary': 'Restringe el avance a ciertas etapas en el modelo de solicitudes',
    'description': """

        El código se utiliza para controlar las etapas permitidas en las solicitudes del modelo 'x_solicitudes_2_0' en Odoo. Al sobrescribir el método 'write' del modelo base, se aplican restricciones para evitar que se cambie el campo 'Etapa' a ciertas etapas bajo ciertas condiciones.

        El código realiza las siguientes comprobaciones:

            Verifica si el modelo es 'x_solicitudes_2_0' y si se está modificando el campo 'Etapa' a una de las siguientes etapas: [Nueva Solicitud, Sin Stock, Preparado, Despachado, Facturar, Cartera Pendiente, Cierre]. Además, verifica si el campo 'requerimiento' es igual a 'Despachar & Facturar' o 'Facturar'.

            Si se cumplen estas condiciones, se realizan las siguientes comprobaciones:

                -Si no se cumplen estas condiciones, el código continúa con el comportamiento predeterminado de la superclase del método 'write'.

                -Si el usuario actual tiene un ID igual a 6 (Comerciales) o 7 (operaciones & Despachos) y se intenta cambiar el campo 'etapa' a las etapas 'Cartera Pendiente' o 'Cierre' (8 o 6 respectivamente), se lanza una excepción de usuario (UserError) indicando que no tiene permiso para realizar esta acción en solicitudes con los requerimientos específicos.

                -Si el campo 'Factura (Que refiere al campo donde se guarda el número de la factura)' no esta establecido y el campo 'Estado' no es igual a "Factura Cancelada", y se intenta cambiar el campo 'Etapa' a las etapas 'Cartera Pendiente' (8) o 'Cierre' (6), se lanza una excepción de usuario (UserError) indicando que no se puede pasar a la etapa de cierre porque se requiere un número de factura establecido.

        El código utiliza las clases y métodos proporcionados por el framework de desarrollo Odoo para implementar estas restricciones personalizadas en el proceso de escritura de las solicitudes del modelo 'x_solicitudes_2_0'.

        El objetivo de esta restricción es asegurar que solo los usuarios autorizados puedan avanzar a ciertas etapas críticas del proceso de solicitudes.

    """,
    'author': 'Aliz Mejia | GitHub: @alizz3',
    'depends': ['base',],  # Dependencias del módulo
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
