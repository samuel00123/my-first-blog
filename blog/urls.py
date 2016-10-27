from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^about/$', views.about_view),
    url(r'^productos/$', views.productos_view),
    url(r'^contacto/$', views.contacto_view),

]
