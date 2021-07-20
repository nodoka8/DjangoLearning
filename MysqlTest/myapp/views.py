from django.shortcuts import render
from django.contrib.auth.decorators import login_required
 
 
def index(request):
    return render(request, 'myapp/index.html')
 
def create(request):
    return render(request, 'myapp/create.html')
    
@login_required
def home(request):
    return render(request, 'myapp/home.html')


