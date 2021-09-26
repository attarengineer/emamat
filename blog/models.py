from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    counter_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={'pid': self.id})
