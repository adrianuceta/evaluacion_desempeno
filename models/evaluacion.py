#models/evaluacion.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación de Desempeño'
    _inherit = ['mail.thread']

    name = fields.Char(string='Título', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True, tracking=True)
    fecha_evaluacion = fields.Date(string='Fecha de Evaluación', required=True, tracking=True)
    comentarios = fields.Text(string='Comentarios', tracking=True)
    puntuacion = fields.Integer(string='Puntuación', required=True, tracking=True)
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string='Estado', default='pendiente', tracking=True)

    @api.constrains('puntuacion')
    def _check_puntuacion(self):
        for record in self:
            if record.puntuacion < 1 or record.puntuacion > 10:
                raise ValidationError('La puntuación debe estar entre 1 y 10')