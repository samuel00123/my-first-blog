from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'', include('ventas.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'documen_root':settings.MEDIA_ROOT,}),

] 
