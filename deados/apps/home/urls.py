from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
    url(r'^login/$', 'login_view', name='vistaLogin'),
    url(r'^logout/$', 'logout_view', name='vistaLogout'),
    url(r'^home/$', 'home_view', name='vistaHome'),
    url(r'^register_institucion/$', 'register_institucion_view', name='vistaRegistro'),
    )