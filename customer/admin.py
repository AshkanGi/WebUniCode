from django.contrib import admin
from .models import Comment, Newsletter


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("brand", "name", "star", "publish")
    list_editable = ['publish']
    search_fields = ("brand",)


admin.site.register(Newsletter)