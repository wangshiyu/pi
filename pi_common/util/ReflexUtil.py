# encoding: utf-8
# !/usr/bin/python3
path = "auth.my_auth.AUTH"

import importlib


class ReflexUtil:

    """
    反射获取实例
    """
    @staticmethod
    def modelGetExample(modelPath,className):
       # model_path, class_name = path.rsplit(".", 1)
        model = importlib.import_module(modelPath)  # 
        example = getattr(model, className)()  # 反射并实例化
        return example
