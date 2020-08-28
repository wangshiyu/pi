# encoding: utf-8
# !/usr/bin/python3
from django.http.response import HttpResponseRedirect

from pi_client.web.web_service.models.PiHttpResponse import PiHttpResponse
from pi_client.web.web_service.views.IndexView import auth
import subprocess

"""
python 代码执行
"""
def pythonRun(request):
    auth_str = auth(request)
    if auth_str != None:
        return HttpResponseRedirect(auth_str)
    code = request.POST.get('code')
    data = {}
    try:
        output = subprocess.check_output(['python','-c',code],
                                         universal_newlines = True,
                                         stderr=subprocess.STDOUT,
                                         timeout=30
                                         )
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as e:
        output = '\r\n'.join(['TIME OUT!!!',e.output])
    data['output'] = output
    return PiHttpResponse.toJson(data)  # ajax请求

# fp = open("./test.py",'w')
# code = """
# print('aaaa')
# """
# fp.writelines(code)
# fp.close()
# result = os.popen("python3 ./test.py") #执行系统命令 返回结果
# res = result.read()
# for line in res.splitlines():
#     print (line)
# result = os.system("python3 ./test.py") #执行系统命令 返回状态
# rf = result >>8
# print(rf)