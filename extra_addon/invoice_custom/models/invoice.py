# my_module/models/invoice.py
import io
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from docx2pdf import convert
from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    invoice_document = fields.Binary(string='Invoice Document')
    invoice_document_name = fields.Char(string='Invoice Document Name')

    @api.multi
    def button_convert_to_pdf(self):
        for invoice in self:
            if invoice.invoice_document:
                # convert the docx file to pdf
                pdf_bytes = convert(io.BytesIO(invoice.invoice_document))
                pdf_writer = PdfFileWriter()
                pdf_reader = PdfFileReader(io.BytesIO(pdf_bytes))
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))
                pdf_path = os.path.splitext(invoice.invoice_document_name)[0] + '.pdf'
                with open(pdf_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
                # update the invoice with the new pdf attachment
                attachment = self.env['ir.attachment'].search([('res_model', '=', 'account.move'), ('res_id', '=', invoice.id), ('name', '=', invoice.invoice_document_name)])
                if attachment:
                    attachment.write({'name': os.path.basename(pdf_path), 'datas': open(pdf_path, 'rb').read()})
                else:
                    self.env['ir.attachment'].create({
                        'name': os.path.basename(pdf_path),
                        'datas': open(pdf_path, 'rb').read(),
                        'res_model': 'account.move',
                        'res_id': invoice.id,
                        'type': 'binary',
                    })
                # remove the temp pdf file
                os.remove(pdf_path)
