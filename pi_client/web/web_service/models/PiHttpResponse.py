# encoding: utf-8
# !/usr/bin/python3
import json
from django.http.response import HttpResponse

"""pi HttpResponse"""

class PiHttpResponse:

    @staticmethod
    def toJson(obj):
        json_ = json.dumps(obj)
        return HttpResponse(json_, content_type="application/json,charset=utf-8")
