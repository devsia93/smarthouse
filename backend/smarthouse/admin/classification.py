from django.contrib import admin

from smarthouse.models import Classification


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    ...
