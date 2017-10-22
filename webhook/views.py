from django.shortcuts import render
import os
# Create your views here.


def webhook(request):
    json = request.POST
    if json:
        if json['commits'][0]['committer']['name'] == 'kekehurry':
            os.system('chomd a+x /usr/www/webhook/webhook.sh')
            os.popen('webhook.sh')
    return
