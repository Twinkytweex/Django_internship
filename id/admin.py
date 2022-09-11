from django.contrib import admin
from id.models import *
from django.utils.html import format_html
from django.contrib.admin.options import StackedInline

admin.site.register(Department)
admin.site.register(PersonalTraits)
admin.site.register(Arival_time)


class Arrivalinlines(StackedInline):
    model = Arival_time
    extra = 0


@admin.register(
    Id,
)
class Model1Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Image"

    list_display = ["image_tag", "first_name", "last_name"]
    inlines = [Arrivalinlines]


class Arival_model_admin(admin.ModelAdmin):
    fields = ["name", "person_number", "check_out"]
