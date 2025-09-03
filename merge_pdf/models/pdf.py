# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
# -----------------------------------------------------------------------------
# Author: hongfeizhou@126.com
# Experienced Odoo developer with many years of expertise.
# Skilled in Python, HTML, and JavaScript for building and customizing solutions.
# -----------------------------------------------------------------------------
import base64
from odoo import models, fields
from odoo.addons.web.controllers.report import ReportController

class MergePdf(models.TransientModel):

    _name = 'merge.pdf'

    pdf_ids = fields.Many2many(comodel_name='ir.attachment')

    def action_merge(self):
        
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': '/download/pdf/%s' % self.id,
        }
        
        