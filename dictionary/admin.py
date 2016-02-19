from django.contrib import admin

from dictionary.models import Definition


class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('-title',)

admin.site.register(Definition, DefinitionAdmin)
