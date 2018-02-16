from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """Configuration for core app."""

    name = 'bureau.apps.core'
    verbose_name = _("Core")
