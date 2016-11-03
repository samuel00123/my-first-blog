from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Producto
from .forms import addProductForm
from django.http import HttpResponseRedirect

def add_product_view (request):
        info= "Inicializando"
        if request.user.is_authenticated():
            if request.method=="POST":
                form= addProductForm(request.POST)
                if form.is_valid():
                        nombre=form.cleaned_data['nombre']
                        descripcion=form.cleaned_data['descripcion']
                        p=Producto()
                        p.nombre=nombre
                        p.descripcion=descripcion
                        p.status=True
                        p.save()
                        info="se guardo satisfactoriamente!!"
                else:
                        info="informacion con datos incorrectos"
                form = addProductForm()
                ctx={'form':form, 'informacion':info}
                return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
            else:
                    form= addProductForm()
                    ctx = {'form':form}
                    return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')
