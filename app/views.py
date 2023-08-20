from django.shortcuts import render

# Create your views here.

def button(request):
    return render(request,'button.html')

def card(request):
    return render(request,'card.html')
