from django.contrib import admin

from smarthouse.models import Indication


@admin.register(Indication)
class IndicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'value')
    list_filter = ('sensor__classification', 'sensor__title')
    search_fields = ('sensor__classification', 'sensor__title')
