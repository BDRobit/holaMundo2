from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def holaMundo(request):
    return HttpResponse("<h1>Hola mundo - esde Django !</h1>")

def primerTemplate(request):
    return render(request,"primer Template.html")

def segundoTemplate(request):
    return render(request,"segundo Template.html")
