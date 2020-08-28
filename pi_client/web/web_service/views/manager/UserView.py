# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from pi_client.cache.PiClientCache import tcpServiceChannelMapCache
from pi_client.web.web_service.views.IndexView import auth
from pi_client.web.web_service.service.UserTcpAddressService import UserTcpAddressService
from pi_db.client.entity.UserTcpAddressEntity import UserTcpAddressEntity
from pi_client.web.web_service.models.AjaxResult import AjaxResult
from pi_client.web.web_service.models.PiHttpResponse import PiHttpResponse
from pi_client.web.web_service.models.dto.UserTcpAddressDTO import UserTcpAddressDTO

"""
TCP连接操作视图
"""
userTcpAddressService = UserTcpAddressService()


### 用户TCP连接地址页
def userTcpAddressIndex(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    # template_view = 'user_tcp_address.html'
    template_view = 'UserTcpAddressList.html'
    return render(request, template_view)

### 获取用户TCP连接地址
def getUserList(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    userId = request.session.get('userId')
    limit = request.GET.get("limit")
    offset = request.GET.get("offset")
    address = request.GET.get("address")
    startTime = request.GET.get("startTime")
    endTime = request.GET.get("endTime")
    userTcpAddressEntity = UserTcpAddressEntity()
    userTcpAddressEntity.limit = limit
    userTcpAddressEntity.offset = offset
    userTcpAddressEntity.userId = userId
    if address != '':
        userTcpAddressEntity.address = address
    if startTime != '':
        userTcpAddressEntity.startTime = startTime
    if endTime != '':
        userTcpAddressEntity.endTime = endTime
    total = userTcpAddressService.getPageCount(userTcpAddressEntity)
    list_ = userTcpAddressService.getPageDate(userTcpAddressEntity)
    result = {}
    rows = list()
    if len(list_) != 0:
        for userTcpAddress in list_:
            userTcpAddressDTO = UserTcpAddressDTO()
            userTcpAddressDTO.id = userTcpAddress.id
            userTcpAddressDTO.address = userTcpAddress.address
            userTcpAddressDTO.createTime = str(userTcpAddress.createTime)
            userTcpAddressDTO.connect = False
            if tcpServiceChannelMapCache.get(userTcpAddressDTO.address) != None:
                userTcpAddressDTO.connect = True
            rows.append(userTcpAddressDTO.toDict())
    result['rows'] = rows
    result['total'] = total
    return PiHttpResponse.toJson(result)  # ajax请求


### 添加用户TCP连接地址
def addUserTcpAddress(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    userId = request.session.get('userId')
    address = request.GET.get('address')
    userTcpAddressEntity = UserTcpAddressEntity()
    userTcpAddressEntity.userId = userId
    userTcpAddressEntity.address = address
    userTcpAddressService.insert(userTcpAddressEntity)
    return PiHttpResponse.toJson((AjaxResult.buildSuccessAjaxResult('ok')))  # ajax请求


### 修改用户TCP连接地址
def updateUserTcpAddress(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    id = request.GET.get('id')
    address = request.GET.get('address')
    userId = request.session.get('userId')
    userTcpAddressEntity = userTcpAddressService.getById(id)
    if userTcpAddressEntity is None or userId != userTcpAddressEntity.userId:
        return PiHttpResponse.toJson((AjaxResult.buildFailAjaxResult('当前用户通过id未获取到数据')))  # ajax请求
    userTcpAddressEntity.address = address
    userTcpAddressService.updata(userTcpAddressEntity)
    return PiHttpResponse.toJson((AjaxResult.buildSuccessAjaxResult("ok")))  # ajax请求


### 删除用户TCP连接地址
def deleteUserTcpAddress(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    id = request.GET.get('id')
    userId = request.session.get('userId')
    userTcpAddressEntity = userTcpAddressService.getById(id)
    if userTcpAddressEntity is None or userId != userTcpAddressEntity.userId:
        return PiHttpResponse.toJson((AjaxResult.buildFailAjaxResult('当前用户通过id未获取到数据')))  # ajax请求
    userTcpAddressService.delete(id)
    return PiHttpResponse.toJson((AjaxResult.buildSuccessAjaxResult("ok")))  # ajax请求
