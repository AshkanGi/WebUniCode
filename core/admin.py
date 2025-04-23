from . import models
from django.contrib import admin
from .models import Team, TeamMember
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

admin.site.register(Team)
admin.site.register(TeamMember)


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['short_about_us_text', 'short_contact_us_text', 'short_address', 'phone', 'email']

    def short_about_us_text(self, obj):
        if len(obj.about_us_text) > 20:
            return obj.about_us_text[:20] + '...'
        return obj.about_us_text

    short_about_us_text.short_description = 'متن درباره ما'

    def short_contact_us_text(self, obj):
        if len(obj.contact_us_text) > 20:
            return obj.contact_us_text[:20] + '...'
        return obj.contact_us_text

    short_contact_us_text.short_description = 'متن تماس با ما'

    def short_address(self, obj):
        if len(obj.address) > 20:
            return obj.address[:20] + '...'
        return obj.address

    short_address.short_description = 'آدرس ما'


@admin.register(models.ContactUs)
class ContactUsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email', 'short_subject', 'short_message', 'get_date_send_jalali']

    def short_subject(self, obj):
        if len(obj.subject) > 20:
            return obj.subject[:20] + '...'
        return obj.subject

    short_subject.short_description = 'موضوع'

    def short_message(self, obj):
        if len(obj.message) > 20:
            return obj.message[:20] + '...'
        return obj.message

    short_message.short_description = 'پیام'

    @admin.display(description='تاریخ ارسال', ordering='date_send')
    def get_date_send_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%d/%m/%Y')
