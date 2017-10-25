from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=100, blank=True, null=True)
    portrait = models.ImageField(
        upload_to='portrait', default='portrait/default.jpg')

    def __str__(self):
        return self.name

    def photo_list(self):
        return ','.join([p.title for p in self.photo_set.all()])


class Photo(models.Model):
    title = models.CharField(max_length=50)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photo/%Y%m')
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title
