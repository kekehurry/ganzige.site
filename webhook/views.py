
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
            r1 = os.system(
                'date ; git fetch --all ; git reset --hard origin/master ; git pull')
            os.system('chmod a+x /usr/www/webhook.sh')
            r2 = os.popen('/usr/www/webhook.sh')
            os.remove('/usr/www/log.txt')
            with open('/usr/www/log.txt', encoding='utf-8') as f:
                f.write(r1.read())
                f.write('/n')
                f.write(r2.read())
        return HttpResponse('post_recieved')
    else:
        return HttpResponse('unknow_post')
