# encoding: utf-8
# !/usr/bin/python3
import importlib
from pi_common.log.LoggingFactory import logger

"""
指令执行器
"""


class DirectiveExecuteHandle:

    @staticmethod
    def execute1(self, imp_module, imp_class):
        # 注意：模块名不包括.py后缀
        # imp_module = 'test_import_class'
        # imp_class = 'ClassA'
        # 方式1：使用__import__()导入模块
        # 导入指定模块，导入时会执行全局方法。
        # ip_module = __import__(imp_module)
        ip_module = importlib.import_module('.', imp_module)
        # dir()查看模块属性
        print(dir(ip_module))
        # 使用getattr()获取imp_module的类
        test_class = getattr(ip_module, imp_class)
        # 动态加载类test_class生成类对象
        cls_obj = test_class()
        # 查看对象属性
        print(dir(cls_obj))

        # hasattr(object, "name") #判断对象有name属性
        for attr in dir(cls_obj):
            # 加载非__前缀的属性
            if attr[0] != '_':
                # 获取导入obj方法。
                class_attr_obj = getattr(cls_obj, attr)
                # 判断类属性是否为函数
                if hasattr(class_attr_obj, '__call__'):
                    # 执行函数
                    class_attr_obj()
                else:
                    # 输出类属性值
                    print(attr, ' type:', type(class_attr_obj), ' value:', class_attr_obj)


    """
    执行对应的模块下的方法
    """

    @staticmethod
    def buildCodeStr(importCodes, initCode, modularName, className, methodName, otherCode):
        exe_code = ""
        import_str = ""
        init_str = ""
        modular_str = ""
        class_str = ""
        method_str = ""
        parameter_str = "parameter_str_replace"
        other_str = ""
        if importCodes != None and len(importCodes) != 0:
            for import_ in importCodes:
                import_str += import_ + " \n"
            import_str +"  \n"
        if initCode != None and len(initCode) != 0:
            init_str = initCode + " \n"
        if className != None and className != "":
            class_str = className + "()."
        if modularName != None and modularName != "":
            modular_str = modularName
        if otherCode != None and len(otherCode) != 0:
            other_str = otherCode + " \n"
        if methodName != None and methodName != "":
            method_str = methodName + "(" + parameter_str + ")" + " \n"

        exe_code = import_str + init_str + class_str + method_str + other_str
        logger.info("execute_method exe_code : " + exe_code)
        return exe_code

    @staticmethod
    def execute_method_codeMapping(exe_str, parameter):
        if parameter != None and len(parameter) != 0:
            parameter_str = ",".join(str(i) for i in parameter)
            exe_str = exe_str.replace("parameter_str_replace", parameter_str)
        else:
            exe_str = exe_str.replace("parameter_str_replace", "")
        logger.info("execute_method exe_str : " + exe_str)
        result =''
        try:
            exec(exe_str)
        except Exception as e:
            print("驱动执行："+e)
        return result
