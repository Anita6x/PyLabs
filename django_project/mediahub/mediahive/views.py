from django.shortcuts import render
from .models import Media
# Create your views here.

def home(request):
    media_items = Media.objects.all()
    return render(request, 'mediahive/home.html', {'media_items': media_items})
