from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tour_agency.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import tour_agency.users.signals  # noqa F401
        except ImportError:
            pass
