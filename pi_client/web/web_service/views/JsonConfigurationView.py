# encoding: utf-8
# !/usr/bin/python3
from django.http import HttpResponseRedirect
from django.shortcuts import render

from pi_client.web.web_service.views.IndexView import auth
from pi_client.web.web_service.service.DBTableColumnJsonServer import DBTableColumnJsonServer

dBTableColumnJsonServer = DBTableColumnJsonServer()


### json插件打开
def jsonViewerIndex(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    type = request.GET.get('type')
    id = request.GET.get('id')
    column = request.GET.get('column')
    jsonStr = dBTableColumnJsonServer.getJsonStr(type, id, column)
    context = {}
    context['jsonStr'] = jsonStr
    template_view = 'json_viewer.html'
    return render(request, template_view, context)

###json数据保存的时候 check一下 非json格式数据无法保存



### python插件打开
def pythonViewerIndex(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    context = {}
    template_view ='python_editor.html'
    return render(request, template_view, context)