from django.db import models

class News(models.Model):
    news_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')

class 