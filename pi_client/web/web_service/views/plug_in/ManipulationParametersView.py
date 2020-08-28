# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponse, HttpResponseRedirect
from pi_client.web.web_service.models.AjaxResult import AjaxResult
from pi_client.control.core.ManipulationParametersControl import ManipulationParametersControl
from pi_common.util.DictUtil import dictCopy

"""
统一操控参数接收
"""


def getAddTo(request):
    username = request.session.get('username')
    if username == None:
        return HttpResponseRedirect('/login/')
    addresssStr = request.GET.get('addresssStr')
    dictDate = {}
    dictCopy(request.GET,dictDate)
    if addresssStr != None:
        addresss = addresssStr.split(',')
        dictDate['addresss'] =addresss
    ManipulationParametersControl.addTo(dictDate)
    return HttpResponse(AjaxResult.buildSuccessAjaxResult("ok"))  # ajax请求


def postAddTo(request):
    username = request.session.get('username')
    if username == None:
        return HttpResponseRedirect('/login/')
    ManipulationParametersControl.addTo(request.POST)
    return HttpResponse(AjaxResult.buildSuccessAjaxResult("ok"))  # ajax请求
