
import os
import json
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if data["commits"][0]["committer"]["name"] == "kekehurry":
            os.system('chmod a+x /usr/www/webhook.sh')
            status = os.popen('nohup /usr/www/webhook.sh &')
        return HttpResponse('post_recieved')
    else:
        return HttpResponse('unknow_post')
