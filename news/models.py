from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)


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
    post_content = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    read_status = models.BooleanField(default=False)
    bookmark_status = models.BooleanField(default=False)
    categories = models.ManyToManyField((Category), blank=True, through='CategoryToPost')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.creation_date.year, self.creation_date.month, self.slug)

class Comment(models.Model):
    pass

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
