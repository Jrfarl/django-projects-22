from urllib import request
from django.contrib import messages
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.
def Index(request):
    return render(request, 'data_app/studentform.html')

def confirm_add(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(
                request, 'There was a problem. Sign up was NOT successful!')
            return render(request, 'data_app/studentform.html', {})

        messages.success(
            request, 'New record was created successfully.')
        return render(request, 'data_app/confirm.html', {'students': students})
    else:
        return render(request, 'data_app/confirm.html', {'students': students})
