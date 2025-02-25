from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Hotels
from .forms import UploadHotelsFile
import json

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html')

def get_data(request):
    data = list(Hotels.objects.values())
    return JsonResponse(data, safe=False)