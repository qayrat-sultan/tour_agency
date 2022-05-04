from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from tour_agency.tour.models import Tour, TourShots


class TourAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tour
        fields = '__all__'


class TourShotsInline(admin.TabularInline):
    model = TourShots
    extra = 1
    readonly_fields = ("get_image",)
    fields = ['name', 'image', 'description']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Rasm"


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourShotsInline]
    form = TourAdminForm


@admin.register(TourShots)
class TourShotsAdmin(admin.ModelAdmin):
    pass
