from django.contrib import admin

# Register your models here.
from .models import Photo, Author, Tag
admin.site.register(Photo)
admin.site.register(Author)
admin.site.register(Tag)
