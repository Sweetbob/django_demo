# Generated by Django 2.1.1 on 2018-09-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0002_article_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_time',
            field=models.TimeField(null=True),
        ),
    ]
