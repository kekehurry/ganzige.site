from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def blog_list(self):
        return ','.join([t.title for t in self.blog_set.all()])


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def blog_list(self):
        return ','.join([t.title for t in self.blog_set.all()])


class Blog(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    pub_time = models.DateTimeField(
        'date published', auto_now_add=True, editable=True)
    author = models.ForeignKey(Author)
    pined = models.BooleanField(default=False)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def tag_list(self):
        return ",".join([p.tag for p in self.tag.all()])

    def get_detail(self):
        return self.detail_set.all()


class Detail(models.Model):
    blog = models.ForeignKey(Blog)
    content = RichTextUploadingField(null=True, blank=True)
    capture = models.CharField(max_length=100, default='No.1')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.capture)
