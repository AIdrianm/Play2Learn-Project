from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

# Register your models here.
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('review', 'created', 'updated')

    def get_readonly_fields(self, request, obj=None):
         if obj:
                return ['created', 'updated']
         
         return ()
    

    """
    list_filter = ('created', 'updated')
    search_fields = ('review',)
    ordering = ('review',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('review',)}
    raw_id_fields = ('author',)
    readonly_fields = ('created', 'updated')
    filter_horizontal = ('categories',)
    fieldsets = (
        (None, {
            'fields': ('review', 'author')
        }),
        ('Categories', {
            'fields': ('categories',)
        }),
        ('Metadata', {
            'fields': ('created', 'updated')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('review', 'author', 'categories')
        }),
    )
    readonly_fields = ('created', 'updated')
"""