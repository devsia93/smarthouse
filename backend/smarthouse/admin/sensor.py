from django.contrib import admin

from smarthouse.models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'room', 'classification',  'unit')
    list_filter = ('room', 'classification')
    search_fields = ('title', 'model')
    ordering = ('room',)
