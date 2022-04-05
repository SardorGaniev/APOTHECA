from django.contrib import admin
from .models import *


class Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug')
    list_display_links = ('id', 'slug')


admin.site.register(Category, Category_Admin)


class Active_substance_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Active_substance, Active_substance_Admin)


class Release_form_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Release_form, Release_form_Admin)


class Brand_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Brand, Brand_Admin)


class Manufacturer_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Manufacturer, Manufacturer_Admin)


class Pharm_group_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Pharm_group, Pharm_group_Admin)


class Country_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Country, Country_Admin)


class Drug_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'country', 'slug')
    list_display_links = ('id', 'name')


admin.site.register(Drug, Drug_Admin)


class Photo_Admin(admin.ModelAdmin):
    list_display = ('id', 'drug')
    list_display_links = ('id', 'drug')


admin.site.register(Photo, Photo_Admin)
