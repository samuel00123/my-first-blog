from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
from .models import Producto
from .forms import contactForm, LoginForm

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect


def index_view (request):
        return render_to_response('blog/index.html',context_instance=RequestContext(request))

def about_view (request):
        mensaje= "Esto es un mensaje desde mi vista"
        ctx={'msg':mensaje}
        return render_to_response('blog/about.html',ctx,context_instance=RequestContext(request))

def productos_view (request):
        prod= Producto.objects.filter(status=True)
        ctx={'productos':prod}
        return render_to_response('blog/productos.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
        info_enviado=False
        email= ""
        titulo=""
        texto=""
        if request.method== "POST":
                formulario = contactForm(request.POST)
                if formulario.is_valid():
                        info_enviado=True
                        email=formulario.cleaned_data ['Email']
                        titulo=formulario.cleaned_data['Titulo']
                        texto=formulario.cleaned_data['Texto']
                        to_admin='samvigotes009@gmail.com'
                        html_content="Informacion recibida de [%s]<br><br><br>***Mensaje***<br><br>%s"%(email,texto)
                        msg= EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
                        msg.attach_alternative(html_content,'text/html')
                        msg.send()
        else:
                formulario=contactForm()
        ctx={'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
        return render_to_response('blog/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
        mensaje=""
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            if  request.method=="POST":
                form=LoginForm(request.POST)
                if form.is_valid():
                    username= form.cleaned_data['username']
                    password= form.cleaned_data['password']
                    usuario  = authenticate(username=username,password=password)
                    if usuario is not None and usuario.is_active:
                        login(request,usuario)
                        return HttpResponseRedirect('/')
                    else:
                        mensaje="usuario y/o password incorrecto"
            form= LoginForm()
            ctx = {'form':form,'mensaje':mensaje}
            return render_to_response('blog/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')
