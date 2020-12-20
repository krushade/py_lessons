from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h2>About</h2>")

def contacts(request, tel_number="", name=''):
    return HttpResponse(f"<h2>Contacts: name: {name}, number: {tel_number}</h2>")

def calc(request, num_1, num_2, symbol):
    if symbol == '+':
        return HttpResponse(str(num_1 + num_2))