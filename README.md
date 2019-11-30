# django-utm-cookies
Django middleware that Store UTM parameters in cookies.

## Installing

Clone or copy repo to root of your project directory. Then add `'utm.middleware.utm_cookies_middleware'` to the end your `MIDDLEWARE` in settings.py. For example:
```python
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    ...
    'utm.middleware.utm_cookies_middleware',
]
```

## Settings

Once you've installed it, you need place some options to `settings.py` in `UTM` section:

```python
UTM = {
    'LIFETIME': 60 * 30,
    'EXCEPT': ['utm_term', 'utm_content'],
}
```

+ **LIFETIME** : (int) Max age of UTM cookies in seconds before we can update they.  
    *Default*: 86400 (24h)

+ **EXCEPT** : (list) Exclude listed parameters from processing.  
    *Default*: []

## Requirements

Tested on Python 3.6 and Django 2.2
