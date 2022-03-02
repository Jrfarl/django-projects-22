from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dice_roll/index.html')

def game(request):
    return render(request, 'dice_roll/game.html')
