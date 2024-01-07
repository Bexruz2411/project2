from django.shortcuts import render
from .models import *

def main(request):
    header = Header.objects.all()
    about = About.objects.all()
    service = Service.objects.all()

    context ={
        'header':header,
        'about':about,
        'service':service
    }
    return render(request, 'index.html', context)