from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    date_membership = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضای خبرنامه'

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    date_send = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        ordering = ["-date_send"]
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    def __str__(self):
        return self.email
