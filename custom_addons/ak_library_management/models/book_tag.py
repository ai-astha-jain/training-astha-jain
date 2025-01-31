# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryBookTags(models.Model):
    _name = 'library.book.tags'
    _description = 'Library Book Tags'


    name = fields.Char(string='Book Tag', required=True)
