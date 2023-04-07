from django.middleware.csrf import get_token

class CsrfTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        get_token(request)
        response = self.get_response(request)
        return response
