from decouple import config

SENTRY_DSN = config('SENTRY_DSN', default='')
{%- if cookiecutter.use_celery == "y" %}
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
{%- endif %}
