from django.contrib import admin
from . import models
# admin.site.register(models.Profil)


@admin.register(models.Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ('name',)
    list_filter = ('created_at', 'update_at')


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', "url")
    list_filter = ('created_at', 'update_at')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ('created_at', 'update_at')


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'update_at')
