from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Project description.
    """
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    """
    A blog category.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title


class Article(models.Model):
    """
    A blog article
    """
    STATUS_OFFLINE = 0
    STATUS_ONLINE = 1
    STATUS_DEFAULT = STATUS_OFFLINE
    STATUS_CHOICES = (
        (STATUS_OFFLINE, 'Offline'),
        (STATUS_ONLINE, 'Online'),
    )

    title = models.CharField(max_length=200)
    article_content = models.CharField(max_length=200, null=True)
    categories = models.ManyToManyField(Category, blank=True, through='CategoryToPost')
    text = models.TextField()
    slug = models.SlugField('slug', max_length=255, unique_for_date='publication_date')
    creation_date = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateTimeField(default=datetime.now(), db_index=True)
    modification_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=STATUS_DEFAULT, db_index=True)
    read_status = models.BooleanField(default=False)
    bookmark_status = models.BooleanField(default=False)
    thumbnail = models.ImageField(blank=True)
    comment_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.creation_date.year, self.creation_date.month, self.slug)


class Comment(models.Model):
    """
    A comment article
    """
    pass


class CategoryToPost(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
