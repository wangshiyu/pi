# encoding: utf-8
# !/usr/bin/python3
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from pi_common.util.MD5Util import getMD5Str
from django import forms
from pi_client.web.web_service.service.UserService import UserService
from pi_db.client.entity.UserEntity import UserEntity

"""
index
"""
userService = UserService()


class UserForm(forms.Form):
    username = forms.CharField()  # 账号
    password = forms.CharField()  # 密码


# 用户登录
def login_view(request):
    username = request.session.get('username')
    if username is not None:
        return HttpResponseRedirect('/index/')

    # 过滤 POST 方法的请求
    if request.method == 'POST':
        userfrom = UserForm(request.POST)
        # 验证表单
        if userfrom.is_valid():
            username = userfrom.cleaned_data['username']
            password = userfrom.cleaned_data['password']
            if password is not None and username is not None:
                md5Str = getMD5Str(password)
                userEntity = UserEntity()
                userEntity.name = username
                userEntity.password = md5Str
                userEntityList = userService.getListByEntity(userEntity)
                if len(userEntityList)==0:
                   return HttpResponse("密码错误或用户不存在")  # ajax请求
            # 将等你信息传递给 Session 对象, 实际应用中不建议这么操作
            request.session['username'] = username
            request.session['userId'] = userEntityList[0].id
            # 跳转到页面
            return HttpResponseRedirect('/index/')
    else:
        # 不是 GET 请求则显示表单
        userfrom = UserForm()
    template_view = 'login.html'
    return render(request, template_view, {'userfrom': userfrom})


# 成功登录之后, 跳转首页
def index_view(request):
    username = request.session.get('username')
    if username == None:
        return HttpResponseRedirect('/login/')
    template_view = 'index.html'
    return render(request, template_view, {'username': username})


# 登出操作
def logout_view(request):
    # 删除 session
    del request.session['username']
    return HttpResponseRedirect('/login/')


def auth(request):
    if request.session.get('username') == None:
        return '/login/'
    return None
