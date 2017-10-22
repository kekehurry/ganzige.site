from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    json = request.POST
    if json and json['commits'][0]['committer']['name'] == 'kekehurry':
        os.system('chmod a+x /usr/www/webhook/webhook.sh')
        status = os.popen('/usr/www/webhook/webhook.sh')
        return HttpResponse('Done!')
    else:
        return HttpResponse('something wrong!')
