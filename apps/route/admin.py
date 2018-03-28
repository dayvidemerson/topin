from django.contrib import admin

from .models import Marker, Line, PointLine, Schedule, Feedback


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
    prepopulated_fields = {'slug': ['name']}

    inlines = [ScheduleInline, PointLineInline]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'reason']
    search_fields = ['name', 'email', 'contact', 'reason']
    list_filter = ['created_at']


admin.site.register(Marker, MarkerAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Feedback, FeedbackAdmin)
