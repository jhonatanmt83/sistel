from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.static import serve
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pc.views.home', name='home'),
    url(r'^arma_tu_pc/$', 'pc.views.arma_tu_pc'),
    url(r'^datos_objeto/(?P<codigo>\d+)/(?P<objeto>\d+)/$', 'pc.views.datos_objeto'),
    url(r'^datos_componentes/(?P<id_placa>\d+)/$', 'pc.views.datos_componentes'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
)
