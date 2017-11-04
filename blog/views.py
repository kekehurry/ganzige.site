from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from .models import Blog, Author, Tag


def index(request, page=1):
    page = int(page)
    blogs = Blog.objects.order_by('-pub_time')
    tag_list = Tag.objects.all().order_by('-pub_time')
    p = Paginator(blogs, 3)
    current_page = p.page(page)
    blogs = current_page.object_list
    pined_blogs = Blog.objects.filter(pined=True).order_by('-pub_time')[:2]

    context = {'blogs': blogs,
               'pined_blogs': pined_blogs, 'current_page': current_page, 'tag_list': tag_list}
    return render(request, 'blog/index.html', context)


def detail(request, page, blog_id, capture_id=1):
    blog = Blog.objects.get(id=blog_id)
    captures = blog.detail_set.all()
    capture = blog.detail_set.get(id=int(capture_id))
    return render(request, 'blog/detail.html', {'blog': blog, 'capture': capture, 'captures': captures, 'page': page})


def author(request, author_id, page=1):
    page = int(page)
    author = Author.objects.get(id=author_id)
    tag_list = Tag.objects.all().order_by('-pub_time')
    blogs = author.blog_set.all().order_by('-pub_time')
    p = Paginator(blogs, 3)
    current_page = p.page(page)
    return render(request, 'blog/author.html', {'blogs': blogs, 'author': author, 'current_page': current_page,'tag_list':tag_list})


def tag(request, tag_id, page=1):
    page = int(page)
    tag = Tag.objects.get(id=tag_id)
    tag_list = Tag.objects.all().order_by('-pub_time')
    blogs = tag.blog_set.all().order_by('pub_time')
    p = Paginator(blogs, 3)
    current_page = p.page(page)
    return render(request, 'blog/tag.html', {'blogs': blogs, 'tag': tag, 'current_page': current_page, 'tag_list': tag_list})
