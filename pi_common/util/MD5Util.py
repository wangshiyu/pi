# encoding: utf-8
# !/usr/bin/python3
import hashlib

"""MD5加密"""


def getMD5Str(obj):
    # 创建md5对象
    hl = hashlib.md5()
    # Tips
    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(obj.encode(encoding='utf-8'))
    return hl.hexdigest()
