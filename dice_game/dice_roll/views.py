from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'dice_roll/index.html')

def game(request):
    return render(request, 'dice_roll/game.html')

def rand_generator(request):
    return render(request, 'rice_roll/rand_generator.html')
    