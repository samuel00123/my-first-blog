from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='vista_principal'),
    url(r'^about/$', views.about_view, name='vista_about'),
    url(r'^productos/$', views.productos_view, name= 'vista_producto'),
    url(r'^contacto/$', views.contacto_view, name='vista_contacto'),
    url(r'^login/$',views.login_view,name='vista_login'),
    url(r'^logout/$',views.logout_view,name='vista_logout'),


]
