from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=255, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', editable=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش', editable=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.name

