
from django.shortcuts import render
from .models import Servicios #importar modelos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'core/index.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def productos(request):
    return render(request,'core/productos.html')

def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]

        message=request.POST["mensaje"]+" "+ request.POST["email"]
        
        email_from=settings.EMAIL_HOST_USER

        recipiente_list=["contactotallerserviexpress@gmail.com"]

        send_mail(subject,message,email_from,recipiente_list)

        return render(request,'core/contacto.html')


    return render(request,'core/contacto.html')


