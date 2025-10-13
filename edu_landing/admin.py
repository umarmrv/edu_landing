from django.contrib import admin
from .models import SiteSettings, HomePageContent, AboutPageContent, Course

# Register your models here.

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "email", "address")

    fieldsets = (
        (None, {
            "fields":("site_name", "logo", "phone", "email", "address")
        }),
    )

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
    list_display = ("title", "price", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)