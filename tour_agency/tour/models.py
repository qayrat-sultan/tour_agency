from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Tour(models.Model):
    title = models.CharField(_("Tur nomi"), max_length=50)
    description = models.TextField(_("Tur haqida ma'lumot"))
    image = models.ImageField(_("Asosiy rasm"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tours:detail", args=[self.id])

    class Meta:
        verbose_name = _("Turistlar uchun Tur")
        verbose_name_plural = _("Turistlar uchun Turlar")


class TourShots(models.Model):
    tour = models.ForeignKey('Tour', verbose_name=_("Tur"), on_delete=models.CASCADE)
    description = models.TextField(_("Tavsif"), default=_("Not exists"))
    image = models.ImageField(_("Tur rasmlari"))
    name = models.CharField(_("Rasm nomi"), max_length=50)

    class Meta:
        verbose_name = _("Tur uchun rasm")
        verbose_name_plural = _("Tur uchun rasmlar")
