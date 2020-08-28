# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponse
"""
系统操作视图
"""
### 系统登录
def login(request):
    if request.method=='GET':
        pass
    if request.method=='POST':
        userName = request.POST.get("username","")
        passWord = request.POST.get("password","")
    # user = authenticate(username=user_name,password=pass_word)
    #     if user is not None:
    #         login(request,user)
    #         return render(request,"index_bk.html")



### 获取系统日志 （管理员才有权限）
def getLogs(request):
    pass
