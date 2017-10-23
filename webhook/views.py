
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
            r1 = os.popen(
                ' git fetch --all ; git reset --hard origin/master ; git pull')
            os.system('chmod a+x /usr/www/webhook.sh')
            r2 = os.popen('nohup /usr/www/webhook.sh > log.txt 2>&1 &')
        return HttpResponse('post_recieved')
    else:
        return HttpResponse('unknow_post')
