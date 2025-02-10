from django.contrib import admin
from .models import Project, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "category", "budget", "project_manager", "star", "created_at", "publish")
    list_editable = ['publish']
    search_fields = ("name", "category__title")
    list_filter = ("category", "created_at")
    ordering = ("-created_at",)

