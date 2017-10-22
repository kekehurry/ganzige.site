
import os
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    json = request.POST
    if json:
        os.system('chmod a+x /usr/www/webhook.sh')
        status = os.popen('/usr/www/webhook.sh')
        return HttpResponse('Done')
