from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse


def webhook(request):
    json = request.POST:
    os.system('sudo chmod a+x /usr/www/webhook/webhook.sh')
    status = os.popen('/usr/www/webhook/webhook.sh')
    return HttpResponse(status)
