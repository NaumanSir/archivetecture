from django.http import JsonResponse
from django.views import View

# Create your views here.
class Arch(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'})