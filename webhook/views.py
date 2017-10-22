from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse


def webhook(request):
    json = request.POST
    if json and json['commits'][0]['committer']['name'] == 'kekehurry':
        os.system('chmod a+x /usr/www/webhook/webhook.sh')
        status = os.popen('/usr/www/webhook/webhook.sh')
        return HttpResponse(status)
    else:
        return HttpResponse('something wrong!')
