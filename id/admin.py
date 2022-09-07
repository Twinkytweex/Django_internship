from django.contrib import admin
from id.models import Id, Department, PersonalTraits, Arival_time
from django.utils.html import format_html

admin.site.register(Department)
admin.site.register(PersonalTraits)
admin.site.register(Arival_time)


@admin.register(
    Id,
)

class Model1Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Image"

    list_display = ["image_tag", "first_name", "last_name"]
