from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from django.http import JsonResponse
from django.core import serializers
from time import time

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getProfile(request):
    print('starting')
    profiles = Profile.objects.all()
    print('gotten')
    print(profiles[0].name)
    profile_values = list(profiles.values())
    return render(request, 'ajax/aj.html', profile_values = profile_values)

class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('btn_text')
        print()
        print(text)
        print()
        if request:
            t = time()
            #return JsonResponse({'seconds': t}, status=200)
        return render(request, 'ajax/aj.html')

class TutorialDataView(View):
    def get(self, request, *args, **kwargs):
        if request:
            profile = Profile.objects.all()
            profile_serializer = serializers.serialize('json', profile)
            return JsonResponse(profile_serializer, safe=False)
        return JsonResponse({'message':'Wrong Validation'})
