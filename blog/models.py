from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class Category (models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = HTMLField(verbose_name='محتوا')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1, verbose_name='نویسنده')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    tags = TaggableManager(verbose_name='تگ')
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', verbose_name='عکس')
    counter_views = models.IntegerField(default=0, verbose_name='بازدید')
    status = models.BooleanField(default=False, verbose_name='انتشار')
    published_date = models.DateTimeField(null=True, verbose_name='تاریخ انتشار')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('-published_date',)
        verbose_name = 'نوشته'
        verbose_name_plural = 'نوشته ها'

    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={'pid': self.id})
