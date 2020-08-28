# encoding: utf-8
# !/usr/bin/python3


def dictCopy(dict1,dict2):
    keys = dict1.keys()
    if len(keys) == 0:
        return False
    else:
        for key in keys:
            dict2[key] = dict1.get(key)