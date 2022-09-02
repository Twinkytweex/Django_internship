from django.contrib import admin
from id.models import Id
from django.utils.html import format_html


@admin.register(Id)
class Model1Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Image"

    list_display = ["image_tag", "first_name", "last_name"]
