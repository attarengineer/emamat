# Generated by Django 3.2.7 on 2021-11-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211102_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.ManyToManyField(to='blog.State', verbose_name='استان'),
        ),
    ]
