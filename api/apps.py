from django.apps import AppConfig
import nltk

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        super().ready()
        nltk.download('punkt')
