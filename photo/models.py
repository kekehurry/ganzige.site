from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def blog_list(self):
        return ','.join([t.title for t in self.blog_set.all()])


class Author(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=100, blank=True, null=True)
    portrait = models.CharField(
        max_length=100, default='http://ganzige.site/media/portrait/default.jpg')

    def __str__(self):
        return self.name

    def photo_list(self):
        return ','.join([p.title for p in self.photo_set.all()])


class Photo(models.Model):
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=50)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title
