from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from .models import Photo


def index(request, page=1):
    page = int(page)
    photos = Photo.objects.order_by('-pub_time')
    p = Paginator(photos, 8)
    current_page = p.page(page)
    recent_photos = current_page.object_list
    if current_page.has_next():
        next_page = page + 1
    else:
        next_page = page
    if current_page.has_previous():
        pre_page = page - 1
    else:
        pre_page = page
    context = {'recent_photos': recent_photos,
               'next_page': next_page, 'pre_page': pre_page, 'page': page}
    return render(request, 'photo/index.html', context)


def detail(request, image_id):
    image = Photo.objects.get(id=image_id)
    return render(request, 'photo/detail.html', {'image': image})
