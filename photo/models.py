from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=50)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photo/%Y%m')
    author = models.CharField(max_length=50, default='杆子哥')

    def __str__(self):
        return self.title
