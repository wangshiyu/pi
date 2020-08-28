# encoding: utf-8
# !/usr/bin/python3
from pi_drive.structure.toJson.BaseJson import BaseJson

"""
通道JSON
(字典结构)
结构：---》 
{
	"IN1": 11,
	"IN2": 12,
	"IN3": 13,
	"IN4": 15
}
"""


class ChannelJson(BaseJson):
    data = None

    def __init__(self):
        self.data = {}

    def addChanne(self, key, value):
        self.data[key] = value
