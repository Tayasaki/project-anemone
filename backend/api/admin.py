from django.contrib import admin

from .models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'zip')
    search_fields = ('name', 'zip')


class LocationCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'location', 'user')
    search_fields = ('location', 'user')


class LocationRatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'location', 'user')
    search_fields = ('location', 'user')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'lan', 'user', 'location', 'date', 'capacity', 'current_capacity')
    search_fields = ('name', 'lan', 'user', 'location')


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user')
    search_fields = ('event', 'user')


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationComment, LocationCommentAdmin)
admin.site.register(LocationRating, LocationRatingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
