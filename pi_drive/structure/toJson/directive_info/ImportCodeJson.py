# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson

"""
引包json
(集合结构)
结构：---》
[
    'from pi_server.drive.L298N.L298NTest import * ',
    'import sys'
]

"""


class ImportCodeJson(BaseJson):
    data = None

    def __init__(self):
        self.data = list()

    def addImport(self, importCode):
        self.data.append(importCode)
