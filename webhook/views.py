from django.shortcuts import render
import os
# Create your views here.


def webhook(request):
    json = request.POST
    if json:
        os.popen('webhook.sh')
    return
