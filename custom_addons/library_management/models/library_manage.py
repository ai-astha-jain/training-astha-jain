# -*- coding: utf-8 -*-

from odoo import models,fields

class LibraryManagement(models.Model):
    _name = "library.manage"
    _description = "Library Manage"

    book_name = fields.Char(string = "Name", required = True)
    type = fields.Char(string="Type of Book")
    price = fields.Integer(string="Book Price")
    publish_date = fields.Date(string="Publishing Date")
    book_id = fields.Char(string="Book Id")

