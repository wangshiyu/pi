# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponse, HttpResponseRedirect
from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_client.web.web_service.views.IndexView import auth
from pi_client.cache.ClientCoreCache import clientCore
from pi_client.web.web_service.models.AjaxResult import AjaxResult
from pi_client.web.web_service.models.PiHttpResponse import PiHttpResponse

"""
TCP连接操作视图
"""


### 获取TCP 连接地址
def getTcpConnectAddress(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    address = tcpServiceChannelMapCache.keys()
    return PiHttpResponse.toJson(AjaxResult.buildSuccessAjaxResult(address))  # ajax请求


### 创建Tcp 连接
def createTcpConnect(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    address = request.GET.get("address", "")
    host = address.split(":")[0]
    port = address.split(":")[1]
    clientCore.createClient(host, int(port))
    return PiHttpResponse.toJson(AjaxResult.buildSuccessAjaxResult('ok'))  # ajax请求


### 关闭Tcp 连接
def closeTcpConnect(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    pass
    address = request.GET.get("address", "")
    tcpChannelCacheEntity = tcpServiceChannelMapCache.get(address)
    if tcpChannelCacheEntity != None:
       tcpChannelCacheEntity.tcpSocketClient.close();
    tcpServiceChannelMapCache.removeChannel(address);
    return PiHttpResponse.toJson(AjaxResult.buildSuccessAjaxResult('ok'))


### 获取Tcp 连接详情
def getTcpConnectInfo(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    pass
