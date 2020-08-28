# encoding: utf-8
# !/usr/bin/python3
from pi_common.constant.enums.AlgorithmInputParameterTypeEnum import AlgorithmInputParameterTypeEnum

"""
参数类型转换
"""


class ParameterTypeChange:
    """
    值类型转换
    """

    @staticmethod
    def valueTypeFormat(key, value, type):
        if value is None:
            print("\"" + key + "\"定义数据为None!")
            return None
        if type is None:
            return value
        elif AlgorithmInputParameterTypeEnum.INT._value_ == type:
            return int(value)
        elif AlgorithmInputParameterTypeEnum.FLOAT._value_ == type:
            return float(value)
        elif AlgorithmInputParameterTypeEnum.BOOL._value_ == type:
            if 'true' == value:
                return True
            else:
                return False
        elif AlgorithmInputParameterTypeEnum.STRING._value_ == type:
            return str(value)
        else:
            raise RuntimeError('未定义的类型!')
