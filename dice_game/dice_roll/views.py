from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, 'dice_roll/index.html')

def game(request):
    return render(request, 'dice_roll/game.html')
    
def results(request):
    user_choice = int(request.GET.get('userChoice'))
    counter = 1
    my_result = []
    while counter <= 5:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1,6)
        roll = dice1 + dice2
        my_result.append(roll)
        counter += 1
    return render(request, 'dice_roll/results.html', {'userChoice': user_choice, 'my_results': my_result})

