from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse


def webhook(request):
    json = request.POST
    if json:
        os.system('chomd a+x /usr/www/webhook/webhook.sh')
        os.popen('webhook.sh')
    return HttpResponse("Hello, world. You're at the polls index.")
