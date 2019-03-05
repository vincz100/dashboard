from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    creation_date = models.DateTimeField('date published')
    modification_date = models.DateTimeField('date modified')
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField((Category), blank=True, null=True, through='CategoryToPost')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.creation_date.year, self.creation_date.month, self.slug)

class Comment(models.Model):
    pass

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
