from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import UserProfile
from django.contrib.auth.models import User

from django.views.generic import View

from django.http import JsonResponse


class UpdateProfile(View):

    def  post(self, request): 

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        website = request.POST.get('website', None)

    
        if request.user.first_name != name:
            request.user.first_name = name
        
        if request.user.email != email:
            request.user.email = email

        if request.user.profile.website != website:
            request.user.profile.website = website

    
        request.user.save()
        request.user.profile.save()


        data = {
            'saved': True
        }

        return JsonResponse(data)



