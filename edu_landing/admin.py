from django.contrib import admin
from django.utils.html import format_html

from .models import SiteSettings, HomePageContent, AboutPageContent, Course

# Register your models here.

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("logo_preview", "site_name", "email", "address")

    fieldsets = (
        (None, {
            "fields":("site_name", "logo", "phone", "email", "address")
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 40px; border-radius: 5px;"/>', obj.logo.url)
        return "(No logo)"
    
    logo_preview.short_description = "Logo"

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ("main_title",)

    fieldsets = (
        (None, {
            "fields":("main_title", "subtitle", "description"),
        }),
    )

    def has_add_permission(self, request):
        if HomePageContent.objects.exists():
            return False
        return True

admin.register(AboutPageContent)
class AboutPageContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

    fieldsets = (
        (None, {
            "fields": ("title", "content"),
        }),
    )

    def has_add_permission(self, request):
        if AboutPageContent.objects.exists():
            return False
        return True
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("img_preview", "title", "price", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    def img_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; border-radius: 5px;"/>', obj.image.url)
        return "(No image)"
    
    img_preview.short_description = "Image"