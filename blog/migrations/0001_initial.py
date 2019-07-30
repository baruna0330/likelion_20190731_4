# Generated by Django 2.2.3 on 2019-07-29 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 29, 6, 48, 36, 40696, tzinfo=utc))),
                ('body', models.TextField()),
                ('writer', models.TextField(default='')),
                ('category', models.CharField(default='public', max_length=200)),
            ],
        ),
    ]
