"""pi_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pi_client.web.web_service.views.plug_in.CarView import move, stop
from pi_client.web.web_service.views.ConnectView import *
from pi_client.web.web_service.views.IndexView import *
from pi_client.web.web_service.views.ManipulateView import *
from pi_client.web.web_service.views.plug_in.ManipulationParametersView import *
from pi_client.web.web_service.views.SystemServerView import *
from pi_client.web.web_service.views.manager.UserTcpAddressView import *
from pi_client.web.web_service.views.JsonConfigurationView import *
from pi_client.web.web_service.views.plug_in.PythonRunView import *

urlpatterns = [
    path('', index_view),  # 默认连接
    # path('index/', index),  # 主页面

    path('admin/', admin.site.urls),

    path('login/', login_view),
    path('index/', index_view),
    path('logout/', logout_view),

    # 用户tcp连接地址
    path('user/tcpAddressIndex/', userTcpAddressIndex),
    path('user/getUserTcpAddress/', getUserTcpAddress),
    path('user/addUserTcpAddress/', addUserTcpAddress),
    path('user/updateUserTcpAddress/', updateUserTcpAddress),
    path('user/deleteUserTcpAddress/', deleteUserTcpAddress),

    # 小车操作
    path('car/carMove/', move),  # ajax 移动
    path('car/carStop/', stop),  # ajax 停止

    # 服务端系统操作
    path('server/getQueues/', getServerQueues),  # 获取服务端所有队列
    path('server/getLogs/', getServerLogs),  # 获取服务端系统日志
    path('server/getTcpConnectAddress/', getServerTcpConnectAddress),  # 获取服务端系统日志

    # 操控主界面
    path('manipulate/index/', manipulateIndex),

    # 操控参数
    path('manipulateParameters/getAddTo/', getAddTo),  # 统一控制参数入口 get 请求
    path('manipulateParameters/postAddTo/', postAddTo),  # 统一控制参数入口 post 请求

    # json插件
    path('jsonViewer/index/',jsonViewerIndex),
    # python插件
    path('pythonViewer/index/',pythonViewerIndex),

    # python插件
    path('pythonRun/',pythonRun),


    ############管理页面###############
    path('connect/getTcpConnectAddress/', getTcpConnectAddress),  # 获取TCP 连接地址
    path('connect/createTcpConnect/', createTcpConnect),  # 创建Tcp 连接
    path('connect/closeTcpConnect/', closeTcpConnect),  # 关闭Tcp 连接
    path('connect/getTcpConnectInfo/', getTcpConnectInfo),  # 获取Tcp 连接详情



]
