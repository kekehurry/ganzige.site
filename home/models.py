from django.db import models

# Create your models here.


class Message_board(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    content = models.TextField(blank=True, null=True, max_length=1000)


class Background(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=100, blank=True)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)

    def __str__(self):
        return self.title
