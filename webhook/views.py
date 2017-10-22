from django.shortcuts import render
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import os
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def send_mail(text):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'kekehurry@163.com'
    to_addr = 'kekehurry@hotmail.com'
    smtp_server = 'smtp.163.com'

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = _format_addr('ganzige <%s>' % from_addr)
    msg['To'] = _format_addr('admin <%s>' % to_addr)
    msg['Subject'] = Header('Information for Github', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


@csrf_exempt
def webhook(request):
    json = request.POST
    os.system('chmod a+x /usr/www/webhook.sh')
    status = os.popen('/usr/www/webhook.sh')
    send_mail(status.readlines())
    return str(status.readlines())
