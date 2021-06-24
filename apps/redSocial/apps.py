from django.apps import AppConfig


class RedsocialConfig(AppConfig):
    name = 'redSocial'


    def ready(self):
        import redSocial.signals