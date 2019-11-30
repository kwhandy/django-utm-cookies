from django.conf import settings

DEFAULTS = {
    'LIFETIME': 60 * 60 * 24,  # max_age in seconds
    'EXCEPT': []  # will not processing
}


def utm_cookies_middleware(get_response):

    def middleware(request):
        utm_settings = getattr(settings, 'UTM', DEFAULTS)
        response = get_response(request)

        for key, value in request.GET.items():
            if key[:4] == 'utm_' \
                    and not key in request.COOKIES.keys() \
                    and not key in utm_settings['EXCEPT']:
                response.set_cookie(key, value,
                                    max_age=utm_settings['LIFETIME'])

        return response

    return middleware
