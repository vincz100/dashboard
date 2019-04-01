# Generated by Django 2.1.7 on 2019-03-31 11:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20190331_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(choices=[(0, 'Diagnostic'), (1, 'PADD'), (2, 'Concertation')], default=0, on_delete=django.db.models.deletion.CASCADE, to='news.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 3, 31, 13, 48, 33, 680842)),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.IntegerField(),
        ),
    ]