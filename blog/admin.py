from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_jalali']
    search_fields = ['title']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')


@admin.register(models.Tag)
class TagAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'views', 'get_created_jalali']
    search_fields = ['title']

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')


@admin.register(models.Article)
class ArticleAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['author', 'short_title', 'alt', 'content', 'views', 'get_created_jalali', 'status']
    list_editable = ['status']
    search_fields = ['title']

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title

    short_title.short_description = 'عنوان مقاله'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')


@admin.register(models.Profile)
class ProfileAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'short_bio', 'show_image', 'alt', 'get_created_jalali']
    search_fields = ['title']

    def short_bio(self, obj):
        if len(obj.bio) > 20:
            return obj.bio[:20] + '...'
        return obj.bio

    short_bio.short_description = 'بیوگرافی'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')
