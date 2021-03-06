# Generated by Django 3.2.7 on 2021-10-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_date'], 'verbose_name': 'تماس با ما', 'verbose_name_plural': 'تماس با ما'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
    ]
