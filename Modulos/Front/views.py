from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.

def landing(request):
    return render(request, "index.html")


def conocenos(request):
    return render(request, "nosotros.html")



def Contacto(request):
    return render(request, "contacto.html")

def contactar(request):
	if request.method=="POST":
		asunto=request.POST["txtAsunto"]
		mensaje=request.POST["txtMensaje"]+" / Email: " + request.POST["txtEmail"]
		email_desde = settings.EMAIL_HOST_USER
		email_para = [request.POST["txtEmail"]]
		send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
		return render(request, "index.html")
	return render(request, "contacto.html")