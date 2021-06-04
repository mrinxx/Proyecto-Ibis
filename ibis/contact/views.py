from django.core.mail.message import EmailMessage
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from ibis.settings import EMAIL_HOST_USER #importo el usuario de correo que va a recibir los correos
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def contact(request):
    contactform=ContactForm()
    is_ok = True
    if request.method=="POST":
        contactform=ContactForm(data=request.POST)
        if contactform.is_valid():
            name=request.POST.get('name','')
            lastname=request.POST.get('lastname','')
            phone=request.POST.get('phonenumber','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            email=EmailMessage(
                "Ibis: Nueva petición de contacto",
                "De {} {} <{}>\n\nEscribió:\n\n{}".format(name,lastname,email,message),
                EMAIL_HOST_USER,['ibis@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                contactform=ContactForm()
            except:
                contactform=ContactForm()
                is_ok = False
    return render(request, "contact/html/contact.html",{'form':contactform, 'ok': is_ok})