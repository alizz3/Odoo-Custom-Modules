{
    'name': 'Payment Date Calculation',
    'version': '1.0',
    'summary': 'El módulo agrega la funcionalidad de cálculo de la fecha límite de pago basada en un plazo seleccionado y la fecha de creación.',

    'description': '''
    Este módulo agrega una funcionalidad clave para controlar los plazos de pago de tus transacciones comerciales. Te permite establecer diferentes opciones de plazos de pago, como 90 días, 45 días y 30 días, o incluso establecer un plazo personalizado.

    Con este módulo, puedes definir fácilmente el plazo de pago adecuado para cada transacción y el sistema calculará automáticamente la fecha límite de pago correspondiente. Esto te ayuda a mantener un seguimiento preciso de las fechas límite de pago y asegurarte de que se cumplan los acuerdos comerciales.

    Además, el módulo es altamente flexible y se puede utilizar en diferentes modelos dentro de Odoo. Puedes aprovechar esta funcionalidad en tus facturas, pedidos de venta, compras u otros documentos comerciales relevantes.

    En resumen, el módulo de cálculo de fecha límite de pago en Odoo simplifica y automatiza el proceso de seguimiento de fechas límite de pago, asegurando que tus transacciones comerciales se realicen dentro de los plazos acordados.''',
    
    'author': 'Aliz Mejía',
    'depends': ['base'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

