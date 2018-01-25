from django.contrib import admin

from .models import Marker, Line, PointLine, Schedule, Route


class MarkerAdmin(admin.ModelAdmin):
    list_display = ['type', 'latitude', 'longitude', 'city']
    search_fields = ['city__name']
    list_filter = ['type', 'city', 'user']
    prepopulated_fields = {'slug': ['name']}


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0


class PointLineInline(admin.TabularInline):
    model = PointLine


class LineAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    search_fields = ['name']
    list_filter = ['user']
    prepopulated_fields = {'slug': ['name']}

    inlines = [ScheduleInline, PointLineInline]


class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'user']
    search_fields = ['name', 'front__name', 'back__name']
    list_filter = ['city', 'user']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Marker, MarkerAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Route, RouteAdmin)
