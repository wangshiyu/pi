# encoding: utf-8
# !/usr/bin/python3
import base64

"""
base64编码
"""


def b64encode(bytes):
    return base64.b64encode(bytes)


"""
base64解码
"""


def b64decode(str):
    return base64.b64decode(str)
