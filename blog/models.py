from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    author = models.CharField(max_length=50)
    pined = models.BooleanField(default=False)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Detail(models.Model):
    blog = models.ForeignKey(Blog)
    content = RichTextUploadingField(null=True, blank=True)
    capture = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.capture)
