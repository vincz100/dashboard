# Generated by Django 2.1.7 on 2019-03-31 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20190331_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 3, 31, 13, 44, 5, 897228)),
        ),
    ]