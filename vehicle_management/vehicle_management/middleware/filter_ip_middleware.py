from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin


class FilterIPMiddleware(MiddlewareMixin):

    def process_request(self, request):
        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')

        if ip not in allowed_ips:
            return PermissionDenied
        return None


