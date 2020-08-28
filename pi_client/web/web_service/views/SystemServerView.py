# encoding: utf-8
# !/usr/bin/python3
from pi_client.control.server.ServerControl import *
"""
服务系统操控
"""
from django.http.response import HttpResponse

### 获取服务端所有连接
def getServerTcpConnectAddress(request):

    return HttpResponse("ok")  # ajax请求

### 获取服务端队列信息
def getServerQueues(request):

    return HttpResponse("ok")  # ajax请求

### 获取服务端日志信息
def getServerLogs(request):
    address = request.GET.get('address')
    logs = ServerControl.getServerLogs(address)
    return HttpResponse("ok")  # ajax请求