from django.contrib import admin

from .models import State, City


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'slug']
    search_fields = ['name', 'abbr']
    prepopulated_fields = {'slug': ['name']}


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'slug']
    search_fields = ['name', 'state__name']
    list_filter = ['state']
    prepopulated_fields = {'slug': ['name']}


admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
