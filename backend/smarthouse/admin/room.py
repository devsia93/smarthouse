from django.contrib import admin

from smarthouse.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    ...
