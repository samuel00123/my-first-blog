from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add/producto/$', views.add_product_view, name='vista_agregar_producto'),
]
