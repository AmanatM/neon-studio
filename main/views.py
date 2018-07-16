from django.shortcuts import render
from .models import Content

# Create your views here.

def index(request):
	context = {'content': Content.objects.all().first()}
	return render(request, 'main/index.html' ,context)