from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    ("draft", "پیش نویس شود"),
    ("published", "منتشر شود"),
)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='نامک')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان برچسب')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='نامک')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='نویسنده مقاله')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی مربوطه')
    title = models.CharField(max_length=150, unique=True, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='نامک')
    content = models.TextField(max_length=200, null=True, blank=True, verbose_name='متا دیسکریپشن')
    description = RichTextUploadingField(verbose_name='محتوای مقاله')
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='articles', verbose_name='برچسب مربوطه')
    thumbnail = models.ImageField(upload_to='images/articles', blank=True, null=True, verbose_name='تصویر مقاله')
    status = models.CharField(choices=STATUS, max_length=10, default='draft', verbose_name='وضعیت')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    bio = models.TextField(max_length=300, help_text='فقط 300 کاراکتر میتونین وارد کنید', null=True, blank=True,
                           verbose_name='بیوگرافی')
    image_profile = models.ImageField(upload_to='images/profiles', help_text='ارتفاع و عرض عکس بهتره 200 پیکسل باشد',
                                      blank=True, null=True, verbose_name='تصویر پروفایل')
    social_instagram = models.CharField(max_length=250, null=True, blank=True, default='https://instagram.com/username',
                                        verbose_name='لینک اینستاگرام')
    social_telegram = models.CharField(max_length=250, null=True, blank=True, default='https://t.me/username',
                                       verbose_name='لینک تلگرام')
    social_whatsapp = models.CharField(max_length=250, null=True, blank=True, default='https://wa.me/0123456789',
                                       verbose_name='لینک واتس اپ')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    def show_image(self):
        if self.image_profile:
            return format_html(f'<img src="{self.image_profile.url}" width="50px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر پروفایل ندارد</h3>')

    def __str__(self):
        return self.user.username