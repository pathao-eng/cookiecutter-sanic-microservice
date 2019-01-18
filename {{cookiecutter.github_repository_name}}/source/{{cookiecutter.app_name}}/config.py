from decouple import config

SENTRY_DSN = config('SENTRY_DSN', default='')
