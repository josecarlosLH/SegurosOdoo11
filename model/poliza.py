#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Dato(models.Model):
	_name = 'seguros.poliza'
	idpoliza = fields.Char('Id poliza', required=True)
	empresa = fields.Char('Empresa',required=True)
	telefono = fields.Integer('Telefono',required=True)
	cliente = fields.Many2one('seguros.cliente','Cliente')
	servicio = fields.Many2many('seguros.servicio',"many2many_default")


