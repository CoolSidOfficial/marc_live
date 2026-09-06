from django.shortcuts import render
from .models import Profile
def home(request):
        profile=Profile.objects.first()
        
        return render(request, "core/home.html",{"my_profile":profile})
