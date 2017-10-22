from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse


def webhook(request):
    json = request.POST
    if json:
        os.poen('chomd a+x /usr/www/webhook/webhook.sh')
        status = os.popen('webhook.sh')
    return HttpResponse(status)
