"""
Definition of views.
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
import json 

@csrf_exempt
def countnumber(request):
    response=""
    if request.method == 'POST':
        number = request.GET['number']
        try:
            Number=sum(int(x) for x in number if x.isdigit())
            #print('Number:{}'.format(Number))
            response = json.dumps([{ 'total': Number}])
        except Exception as E:
            print(E)
            response = json.dumps([{ 'Error': 'cannot count the number'}])
        pass
    return HttpResponse(response, content_type='text/json')