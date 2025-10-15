from django.contrib import admin
from images import models
# Register your models here.

@admin.register(models.Image)
class imageAdmin(admin.ModelAdmin):
    list_display=["title","slug","image","created"]
    list_filter=["created"]