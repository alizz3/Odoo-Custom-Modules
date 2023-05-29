{
    'name': 'Payment Date Calculation',
    'version': '1.0',
    'summary': 'El módulo agrega la funcionalidad de cálculo de la fecha límite de pago basada en un plazo seleccionado y la fecha de creación. Proporciona campos para seleccionar el plazo de pago y muestra automáticamente la fecha límite de pago calculada. El campo "create_date" debe estar presente para garantizar el correcto funcionamiento.',
    'description': '''El módulo proporciona la funcionalidad de cálculo de la fecha límite de pago basada en un plazo de pago seleccionado y la fecha de creación.

    El módulo incluye un campo de selección llamado "Plazo de pago" que permite al usuario elegir entre diferentes opciones de plazos de pago. Además, se muestra un campo que automáticamente calcula y muestra la fecha límite de pago en función del plazo de pago seleccionado y la fecha de creación, la fecha límite de pago se calcula sumando los días del plazo de pago a la fecha de creación. 

    Es importante tener en cuenta que el campo "create_date" debe estar presente en la vista para que el cálculo de la fecha límite de pago funcione correctamente. Aunque este campo no es necesario que sea visible para los usuarios, debe estar presente en el modelo para evitar errores en el cálculo.''',
    'author': 'Aliz Mejía',
    'depends': ['base'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

