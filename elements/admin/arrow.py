from django.contrib import admin

from elements.models.arrow import Arrow


@admin.register(Arrow)
class ArrowAdmin(admin.ModelAdmin):
    list_display = ('block_from', 'block_to')
