from django.contrib import admin

from . import models


@admin.register(models.Spec)
class SpecAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.CrashType)
class CrashTypeAdmin(admin.ModelAdmin):

    list_display = ('name', 'get_specs')
    list_filter = ('specs',)
    search_fields = ('name', 'specs__name')
    filter_horizontal = ('specs',)

    def get_specs(self, obj):
        return ', '.join([i for i in obj.specs.values_list('name', flat=True)])

    get_specs.short_description = 'Специализация'
