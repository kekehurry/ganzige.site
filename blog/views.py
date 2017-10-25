from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from .models import Blog, Author, Tag


def index(request, page=1):
    page = int(page)
    blogs = Blog.objects.order_by('-pub_time')
    p = Paginator(blogs, 3)
    current_page = p.page(page)
    if current_page.has_next():
        next_page = page + 1
    else:
        next_page = page
    if current_page.has_previous():
        pre_page = page - 1
    else:
        pre_page = page
    latest_blogs = current_page.object_list
    pined_blogs = Blog.objects.filter(pined=True).order_by('-pub_time')[:2]

    context = {'latest_blogs': latest_blogs,
               'pined_blogs': pined_blogs, 'next_page': next_page, 'pre_page': pre_page, 'page': page}
    return render(request, 'blog/index.html', context)


def detail(request, blog_id, capture_id=1):
    blog = Blog.objects.get(id=blog_id)
    captures = blog.detail_set.all()
    capture = blog.detail_set.get(id=int(capture_id))
    return render(request, 'blog/detail.html', {'blog': blog, 'capture': capture, 'captures': captures})


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    blogs = author.blog_set.all().order_by('-pub_time')
    return render(request, 'blog/author.html', {'blogs': blogs, 'author': author})


def tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    blogs = tag.blog_set.all().order_by('-pub_time')
    return render(request, 'blog/tag.html', {'blogs': blogs, 'tag': tag})
