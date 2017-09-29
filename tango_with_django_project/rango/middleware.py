from django.conf import settings
import requests

class StackOverflowMiddleware(object):
    def process_exception(self, request, exception):
        return None