# encoding: utf-8
# !/usr/bin/python3

import pickle


def objToByts(obj):
    return pickle.dumps(obj)


def bytsToObj(byts):
    return pickle.loads(byts)


"""
字典转python对象
"""


def dictToObj(dict, class_):
    case = class_()
    case.__dict__ = dict
    return case


"""
集合嵌套字典转集合嵌套python对象
"""


def listDictToListObj(list_, class_):
    objList = list()
    if (len(list_) > 0):
        for dict in list_:
            case = class_()
            case.__dict__ = dict
            objList.append(case)
    return objList
