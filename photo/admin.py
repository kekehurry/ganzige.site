from django.contrib import admin

# Register your models here.
from .models import Photo, Author
admin.site.register(Photo)
admin.site.register(Author)
