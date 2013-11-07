# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Made.com. All Rights Reserved
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

{
    "name": "Report Spreadsheet",
    "version": "0.1",
    "description": """
    This module enables to create reports in xls or csv format using Python.
    Suggestions & Feedback to: choplin.mat@gmail.com
    This version is adapted for the last version of OpenERP (v7 and trunk)
    """,
    "author": "Made.com",
    "license": 'AGPL-3',
    'category': 'Generic Modules/Reporting',
    "depends": ['base'],
    "init_xml": [],
    "update_xml": [
        'security/report_spreadsheet.xml',
        'security/ir.model.access.csv',
        'view/report_config_view.xml',
        'view/report_param.xml',
        'demo/report_config_demo.xml',
    ],
    "demo_xml": [
        'demo/report_config_demo.xml',
    ],
    "test": [
        'tests/report_config_demo_test.xml',
        'tests/create_report.yml',
    ],
    "installable": True,
    "active": False
}
