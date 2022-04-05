from django.contrib import admin
from .models import *


class Banner_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Banner, Banner_Admin)


class Feedback_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_display_links = ('id', 'phone')


admin.site.register(Feedback, Feedback_Admin)
