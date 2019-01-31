from django.http import JsonResponse
from django.views import View
from .models import Arch
import json

# Create your views here.
class Archs(View):
    def get(self, request):
        archs = list(Arch.objects.values().all())
        return JsonResponse({'status': 'ok', "Archs": archs})
    
    def post(self, request):
        body = json.loads(request.body.decode())
        print(body, type(body))
        Arch.objects.create(
            name = body['name'],
            yrbuilt = body['yrbuilt'],
            location = body['location'],
            desc = body['desc'],
        )
        return JsonResponse({'status': 'ok', "message": "This is a post."})