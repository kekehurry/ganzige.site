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
    context = {'recent_photos': recent_photos,
               'current_page': current_page}
    return render(request, 'photo/index.html', context)


def detail(request, page, image_id):
    image = Photo.objects.get(id=image_id)
    return render(request, 'photo/detail.html', {'image': image, 'page': page})
