from django.contrib import admin
from .models import Cars
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ['id']

    def get_photo(self, object): return mark_safe(f"<img src='{object.photo.url}' width=50>")

    def get_link(self, object): return mark_safe("<a href=%s>link</a>" % object.link)

    list_display = ['manufacturer', 'years_of_production', 'platform', 'get_link', 'get_photo']

admin.site.register(Cars, PostAdmin)


