from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "hotel_project.utils"

    def ready(self):
        from . import checks  # noqa
