from django.contrib import admin

# Register your models here.
from .models import Blog, Detail


class DetailInline(admin.StackedInline):
    model = Detail
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [DetailInline]


admin.site.register(Blog, BlogAdmin)
