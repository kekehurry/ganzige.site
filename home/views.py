from django.shortcuts import render

# Create your views here.

from blog.models import Blog
from photo.models import Photo
from .models import Message_board, Background


def home(request):
    blogs = Blog.objects.order_by('-pub_time')[:4]
    recent_photos = Photo.objects.order_by('-pub_time')[:8]
    background = Background.objects.order_by('-pub_time')[:1]
    message = '欢迎各位小伙伴前来吐槽~'
    if request.POST:
        message = '留言已提交，谢谢您的关注！'
        m = Message_board()
        m.content = request.POST['message']
        m.title = m.content[:20]
        m.save()
    context = {'blogs': blogs, 'message': message,
               'recent_photos': recent_photos, 'background': background}
    return render(request, 'home/home.html', context)
