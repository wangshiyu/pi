# encoding: utf-8
# !/usr/bin/python3
"""
Map结构 字典实现
"""
from pi_common.exception import PiException


class Map:
    data = None

    def __init__(self) -> object:
        self.data = {}

    def get(self, key):
        if key == None:
            return None
        return self.data.get(key)

    def put(self, key, value):
        if key == None or value == None:
            raise PiException.NullException()
        self.data[key] = value

    def clear(self):
        return self.data.clear()

    def removeChannel(self, key):
        del self.data[key]

    def isEmpty(self):
        return len(self.data) == 0

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()


if __name__ == "__main__":
    map = Map();
    map.put(None, None)
