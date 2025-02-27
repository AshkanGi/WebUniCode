from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='نامک', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='نامک')
    name = models.CharField(max_length=100, verbose_name='نام مشتری')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ')
    budget = models.CharField(max_length=100, verbose_name='بودجه')
    project_manager = models.CharField(max_length=60, verbose_name='مدیر پروژه')
    place = models.CharField(max_length=100, verbose_name='محل')
    website = models.URLField(max_length=200, verbose_name= 'وب سایت', blank=True, null=True)
    star = models.IntegerField(verbose_name='امتیاز')
    main_image = models.ImageField(upload_to='project', verbose_name='عکس اصلی')
    description = RichTextUploadingField(verbose_name='محتوای پروژه', default='')
    publish = models.BooleanField(default=False, verbose_name='مجوز انشتار')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def __str__(self):
        return f"{self.name} - {self.website}"
