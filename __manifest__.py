# evaluacion_desempeno/__manifest__.py
{
'name': 'Evaluación de desempeño',
'version': '1.0',
'summary': 'Módulo para evaluar el desempeño individual de los empleados',
'category': 'Human Resources',
'author': 'Adrián Uceta Gamaza',
'website': 'https://tuweb.com',
'license': 'LGPL-3',
'depends': ['base','hr'],
'icon': '/evaluacion_desempeno/static/description/icon53.png',
'data': [
'views/evaluacion_views.xml',
'security/ir.model.access.csv',
],
'assets': {
'web.assets_backend': [
'evaluacion_desempeno/static/src/css/styles.css',
],
},
'application': True,
'installable': True,
'auto_install': False,
'description': """
Módulo de Odoo para la evaluación de desempeño de empleados,
incluyendo vistas Kanban y formulario detallado.
"""
}