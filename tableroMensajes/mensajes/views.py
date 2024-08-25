from django.shortcuts import render
from .models import Mensaje 

# Create your views here.

def mensajes (request):
    recibidos =  Mensaje.objects.all()

    return render(request, 'mensajes/mensajes.html', {'mensajes':recibidos})