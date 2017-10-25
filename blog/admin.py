from django.contrib import admin

# Register your models here.
from .models import Author, Blog, Detail, Tag


class DetailInline(admin.StackedInline):
    model = Detail


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tag_list', 'pub_time')
    list_filter = ['author', 'tag']
    inlines = [DetailInline]


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'blog_list']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'blog_list']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
