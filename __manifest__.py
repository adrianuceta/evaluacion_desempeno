{
'name': 'Evaluación de desempeño',
'version': '1.0',
'summary': 'Módulo para evaluar el desempeño de los empleados',
'category': 'Human Resources',
'author': 'Adrián Uceta Gamaza',
'website': 'https://tuweb.com',
'license': 'LGPL-3',
'depends': ['base', 'mail', 'hr'],
'icon': '/evaluacion_desempeno/static/description/icon53.png',
'data': [
'views/evaluacion_views.xml',
'security/ir.model.access.csv',
],
'application': True,
'installable': True,
'auto_install': False,
'assets': {
    'web.assets_backend': [
        '/evaluacion_desempeno/static/src/css/styles.css',
    ],
},
'description': """
Módulo de Odoo para la evaluación del desempeño de los empleados,
incluyendo vistas Kanban y formulario detallado.
"""
}