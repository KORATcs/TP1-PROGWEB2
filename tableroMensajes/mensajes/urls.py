from django.urls import path 
from .views import mensajes

app_name = 'mensajes'
urlpatterns = [
    path(
        'recibidos/', mensajes, name = 'mensaje'
    )
]