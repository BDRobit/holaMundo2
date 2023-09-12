from django.shortcuts import render

# Create your views here.

def llamarTemplate(request):
    data = {"nombre":"hector",
    "apellido":"sanzana"}
    return render(request,'templatesApp/vista1.html',data)

def infoUsuario(request):
    data = {
        "nombre":"hector",
        "id":"sanzana",
        "correo": "h.sanzana@gmail.com"}
    return render(request,'templatesApp/infoUsuario.html',data)