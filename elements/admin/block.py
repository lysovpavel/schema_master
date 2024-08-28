from django.contrib import admin

from elements.models.block import Block


@admin.register(Block)  # type: ignore
class BlockAdmin(admin.ModelAdmin):
    list_display = ('coordinate_x', 'coordinate_y', 'height', 'width')

