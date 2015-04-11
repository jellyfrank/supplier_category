#-*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Autor:Kevin Kong (kfx2007@163.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields,models,_,api

class supplier_category(models.Model):
	_name="supplier.category"

	@api.one
	def name_get(self):
		if self.parent_id:
			name = self.parent_id.name +"/"+self.name
		else:
			name = self.name
		return (self.id,name)

	@api.one 
	def _get_display_name(self):
		result = self.name_get();
		if len(result):
			self.complete_name = result[0][1]

	name = fields.Char('Category Name')
	complete_name = fields.Char('Display Name',compute="_get_display_name")
	parent_id = fields.Many2one('supplier.category','Parent Category')
	child_id = fields.One2many('supplier.category','parent_id','Child Category')
	parent_left = fields.Integer('Parent Left')
	parent_right = fields.Integer('Parent Right')

	_parent_id='parent_id'

class suppplier(models.Model):
	_inherit="res.partner"

	category = fields.Many2one('supplier.category')