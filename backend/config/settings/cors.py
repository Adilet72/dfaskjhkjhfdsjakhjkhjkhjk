
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'accept-language',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://django-server-production-8abc.up.railway.app$",
    r"^http://127\.0\.0\.1(:\d+)?$",  # локальный сервер
    r"^http://localhost(:\d+)?$",  # локальный сервер с localhost
]
CSRF_TRUSTED_ORIGINS = [
    'https://django-server-production-8abc.up.railway.app',
]


