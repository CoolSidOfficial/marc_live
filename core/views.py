from django.shortcuts import render
from .models import Profile
from .models import Website
def home(request):
        
        
        return render(
          request, "core/home.html",
    {
        "my_profile": Profile.objects.first()
,
        "websites": Website.objects.all(),
    }
)