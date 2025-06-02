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
    r"^https://adilet72\.github\.io/Islam-ai-checkar-ts/?$",  # GitHub Pages точечный
    r"^https://adilet72\.github\.io$",                       # общий адрес GitHub Pages
    r"^http://127\.0\.0\.1(:\d+)?$",
    r"^http://localhost(:\d+)?$",
    r"^https://django-server-production-8abc.up.railway.app$",
]
CSRF_TRUSTED_ORIGINS = [
    'https://django-server-production-8abc.up.railway.app',
    'https://adilet72.github.io',
]
