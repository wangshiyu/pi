# encoding: utf-8
# !/usr/bin/python3
"""
参数解析器

#?       当前key 为key
#&=*     *为key
#df=*    *为默认值
"""


class ParameterAnalysis:

    @staticmethod
    def mapping(key, value, dict):
        valueStr = str(value)
        if '|' in valueStr:
            valueStrS = valueStr.split('|')
            for i in valueStrS:
                if '#?' in i:
                    value_ = dict.get(key)
                    if value_ is not None:
                        return value_
                if '#&=' in i:
                    key_ = i.replace('#&=', '')
                    value_ = dict.get(key_)
                    if value_ is not None:
                        return value_
                if '#df=' in i:
                    value_ = i.replace('#df=', '')
                    if value_ is not None:
                        return value_
            return value
        else:
            if '#?' in valueStr:
                value_ = dict.get(key)
                if value_ is not None:
                    return value_
            if '#&=' in valueStr:
                key_ = valueStr.replace('#&=', '')
                value_ = dict.get(key_)
                if value_ is not None:
                    return value_
            if '#df=' in valueStr:
                value_ = valueStr.replace('#df=', '')
                if value_ is not None:
                    return value_
            else:
                return value
