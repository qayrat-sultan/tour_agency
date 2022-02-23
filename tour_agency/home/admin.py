from django.contrib import admin
from django.utils.safestring import mark_safe

from tour_agency.home.models import Tour, TourShots


class TourShotsInline(admin.TabularInline):
    model = TourShots
    extra = 1
    readonly_fields = ("get_image",)
    fields = ['name', 'image', 'description']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Rasm"


@admin.register(Tour)
class Tur(admin.ModelAdmin):
    inlines = [TourShotsInline]


@admin.register(TourShots)
class Tur(admin.ModelAdmin):
    pass
