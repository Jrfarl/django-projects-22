from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'KeepWorking/index.html')

def projects(request):
    first_name = request.GET.get('first') + ' ' + request.GET.get('last')
    
    return render(request, 'KeepWorking/projects.html', {'first' : first_name})
