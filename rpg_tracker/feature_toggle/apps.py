from django.apps import AppConfig


class FeatureToggleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpg_tracker.feature_toggle'
