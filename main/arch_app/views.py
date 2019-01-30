from django.http import JsonResponse
from django.views import View

# Create your views here.
class Arch(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'})
    
    def post(self, request):
        print(request.body)
        return JsonResponse({'status': 'ok', "message": "This is a post."})