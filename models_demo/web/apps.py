from django.apps import AppConfig

from models_demo import web


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models_demo.web'
