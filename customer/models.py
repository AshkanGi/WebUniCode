from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    brand = models.CharField(max_length=50, verbose_name='برند')
    body = models.TextField(max_length=100, verbose_name='متن')
    star = models.IntegerField(verbose_name='امتیاز')
    image = models.ImageField(upload_to='image/customer', verbose_name='عکس')
    alt = models.CharField(max_length=50, null=True, blank=True, verbose_name='توضیح عکس')
    publish = models.BooleanField(default=False, verbose_name='مجوز قرار دادن')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.name} - {self.brand}'


class Newsletter(models.Model):
    email = models.EmailField(max_length=225, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'خبرنامه ها'

    def __str__(self):
        return self.email
