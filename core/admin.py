from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['email', 'copy_right', 'instagram_link', 'telegram_link']


@admin.register(models.Newsletter)
class NewsletterAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email', 'get_date_membership_jalali']

    @admin.display(description='تاریخ عضویت', ordering='date_membership')
    def get_date_membership_jalali(self, obj):
        return datetime2jalali(obj.date_membership).strftime('%a, %d %b %Y')


@admin.register(models.ContactUs)
class ContactUsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['full_name', 'email', 'short_subject', 'short_message', 'get_date_send_jalali']

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
        return datetime2jalali(obj.date_send).strftime('%a, %d %b %Y')
