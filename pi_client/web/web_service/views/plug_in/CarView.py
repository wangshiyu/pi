# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponse,HttpResponseRedirect
from pi_client.control.car.CarControl import CarControl
from pi_client.control.car.SystemServerControl import SystemServerControl
from pi_drive.constant.enums.DirectiveTypeEnum import DirectiveTypeEnum
from pi_client.web.web_service.models.AjaxResult import AjaxResult
"""
小车控制视图
"""


# 移动
def move(request):
    username = request.session.get('username')
    if username == None:
        return HttpResponseRedirect('/login/')
    yl = request.GET.get('yl')
    yr = request.GET.get('yr')
    ruler_yl = request.GET.get('ruler_yl')
    ruler_yr = request.GET.get('ruler_yr')
    addresss = request.GET.get('addresss').split(',')
    print('move yl='+ yl +"  yr"+yr)
    CarControl.move(yl,yr,ruler_yl,ruler_yr,addresss,username)
    return HttpResponse(AjaxResult.buildSuccessAjaxResult("ok"))  # ajax请求


# 停止
def stop(request):
    # CarControl.stop()
    addresss = request.GET.get('addresss').split(',')
    SystemServerControl.cleanServerQueue({DirectiveTypeEnum.Car_Directive_Left._value_,DirectiveTypeEnum.Car_Directive_Right._value_},addresss)
    return HttpResponse("ok")  # ajax请求
