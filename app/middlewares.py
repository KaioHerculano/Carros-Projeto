from django.utils.deprecation import MiddlewareMixin

class CrossOriginOpenerPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Adiciona o cabeçalho 'Cross-Origin-Opener-Policy' com o valor 'same-origin'
        response['Cross-Origin-Opener-Policy'] = 'same-origin'
        return response
