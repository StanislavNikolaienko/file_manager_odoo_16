from odoo import api, fields, models


class FileManager(models.Model):
    _name = "file.manager"
    _description = "File manager"

    file_name = fields.Char(string="File name")
    upload_file = fields.Binary(string="Upload file")
    upload_date = fields.Datetime(string="Upload Date")
