from django.shortcuts import render

# Create your views here.

from .models import Blog


def index(request, page=1):
    num = len(Blog.objects.all())
    blogs = Blog.objects.order_by('-pub_time')
    page = int(page)
    if page < int(num / 3) + 1:
        next_page = page + 1
    else:
        next_page = page
    if page >= 2:
        pre_page = page - 1
    else:
        pre_page = 1
    latest_blogs = blogs[(page - 1) * 3:page * 3]
    pined_blogs = Blog.objects.filter(pined=True).order_by('-pub_time')[:2]

    context = {'latest_blogs': latest_blogs,
               'pined_blogs': pined_blogs, 'next_page': next_page, 'pre_page': pre_page, 'page': page}
    return render(request, 'blog/index.html', context)


def detail(request, blog_id, capture_id=1):
    blog = Blog.objects.get(id=blog_id)
    captures = blog.detail_set.all()
    capture = blog.detail_set.get(id=int(capture_id))
    return render(request, 'blog/detail.html', {'blog': blog, 'capture': capture, 'captures': captures})
