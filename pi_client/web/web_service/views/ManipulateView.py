# encoding: utf-8
# !/usr/bin/python3
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from pi_client.web.web_service.views.IndexView import auth
import json


### 操控主界面
def manipulateIndex(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    userId = request.session.get('userId')
    addressStr = request.GET.get('address')
    context = {}
    context['addresssStr'] = addressStr
    template_view = 'manipulate.html'
    return render(request, template_view,context)
