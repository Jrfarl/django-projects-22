from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'pw/index.html')

def new_pw(request):
    the_new_pw = ''
    length = int(request.GET.get('length', 8))

    pw_list = list('abcdefghijklmnopqrstuvwxyz')

    uppercase = request.GET.get('uppercase')
    if uppercase:
        pw_list.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special = request.GET.get('special')
    if special:
        pw_list.extend('!@#$%^&*()-_=+[{]}\\/?:,\'~`.')
    numbers = request.GET.get('numbers')
    if numbers:
        pw_list.extend('1234567890')

    for i in range(length):
        the_new_pw += random.choice(pw_list)

    return render(request, 'pw/new_pw.html', {'length': length, 'uppercase': uppercase,
     'special': special, 'numbers': numbers, 'new_pw': the_new_pw})
