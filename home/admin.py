from django.contrib import admin

# Register your models here.
from .models import Message_board, Background

admin.site.register(Message_board)
admin.site.register(Background)
