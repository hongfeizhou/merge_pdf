# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import json

from odoo import http
from odoo.http import request
from odoo.tools.pdf import merge_pdf


class ReportController(http.Controller):

    @http.route(['/download/pdf/<int:id>'], type='http', auth="user")
    def pdf_download(self, id):
        pdfs = request.env['merge.pdf'].browse(id)
        pdf_datas = []
        for pdf in pdfs.pdf_ids.sorted(lambda x: x.id):
            pdf_datas.append(base64.b64decode(pdf.datas))
        pdf_datas = merge_pdf(pdf_datas)
        filename = '1.pdf'
        return request.make_response(
            pdf_datas,
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename={filename}')
            ]
        )