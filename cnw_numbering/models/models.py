# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class /data/igu_it_dev/cnw_numbering(models.Model):
#     _name = '/data/igu_it_dev/cnw_numbering./data/igu_it_dev/cnw_numbering'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class CNW_DOCnumbering(models.Model):
	_name = "cnw.numbering"
	_description = "Document Numbering"

	name 			= fields.Char("Doc Numbering")
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	suffix 			= fields.Char("Suffix",required=True)
	iyear			= fields.Char("Year",required=True)
	imonth			= fields.Char("Month",required=True)
	numbering 		= fields.Integer("Numbering",default=0)
	user_update		= fields.Many2one("res.users")


class CNW_numberingWiz(models.TransientModel):
	_name  = "cnw.numbering.wizard"
	_description ="NUmbering WIzard"
	suffix = fields.Char("Suffix")
	docdate = fields.Date("Date",required=True)
 
	def getnumbering(self,suffix,docdate):
		print("test parameter" )
		print(suffix)
		print(docdate)

 

		numb = self.env["cnw.numbering"].search([("company_id","=",self.env.user.company_id.id),
													("suffix","=",suffix),
													("iyear","=" ,docdate.year),
													("imonth","=" ,docdate.month),
													]).numbering
 
		numbering = numb+1
		if numb==0:
			self.env["cnw.numbering"].create({"company_id":self.env.user.company_id.id,
													"suffix":suffix,
													"iyear":docdate.year,
													"imonth": docdate.month,
													"numbering":numbering})

		else:
			record = self.env['cnw.numbering'].search([("company_id","=",self.env.user.company_id.id),
													("suffix","=",suffix),
													("iyear","=" ,docdate.year),
													("imonth","=" ,docdate.month),
													])

			record.write({"numbering":numbering})
		print (type(docdate))
		result = suffix + docdate.strftime("%y") + docdate.strftime("%m") + str(numbering).rjust(4,'0')
		print(result)
		return result





	def getnumbering2(self):
		self.getnumbering(self.suffix,self.docdate)
