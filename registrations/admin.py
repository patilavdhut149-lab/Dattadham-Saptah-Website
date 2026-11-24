from django.contrib import admin
from .models import Registration, SiteContent, ProgramItem

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "mobile", "other_service", "whatsapp_group", "created_at")
    search_fields = ("full_name", "mobile", "address")
    list_filter = ("other_service", "whatsapp_group", "created_at")
    readonly_fields = ("created_at",)

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(ProgramItem)
class ProgramItemAdmin(admin.ModelAdmin):
    list_display = ("section", "title", "sort_order")
    list_filter = ("section",)
    ordering = ("sort_order",)
