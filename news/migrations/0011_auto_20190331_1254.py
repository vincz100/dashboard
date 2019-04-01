# Generated by Django 2.1.7 on 2019-03-31 10:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190331_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytopost',
            name='article',
        ),
        migrations.RemoveField(
            model_name='categorytopost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='news.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 3, 31, 12, 53, 44, 718908)),
        ),
        migrations.DeleteModel(
            name='CategoryToPost',
        ),
    ]