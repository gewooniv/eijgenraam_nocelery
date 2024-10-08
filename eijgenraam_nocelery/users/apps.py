#!/usr/bin/env python3
import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "eijgenraam_nocelery.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import eijgenraam_nocelery.users.signals  # noqa: F401
