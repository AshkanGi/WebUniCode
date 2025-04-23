from django.contrib import admin
from .models import Project, Category
from jalali_date import datetime2jalali


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "category", "budget", "content", "project_manager", "star", 'alt',  'get_created_jalali', "publish")
    list_editable = ['publish']
    search_fields = ("name", "category__title")
    list_filter = ("category", "created_at")
    ordering = ("-created_at",)

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')
