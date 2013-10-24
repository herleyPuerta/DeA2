from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
    url(r'^login/$', 'login_view', name='vistaLogin'),
    url(r'^logout/$', 'logout_view', name='vistaLogout'),
    url(r'^home/$', 'home_view', name='vistaHome'),
    url(r'^register_institucion/$', 'register_institucion_view', name='vistaRegistro'),
    url(r'^register_institucion_name/$', 'register_institucion_name_view', name='vistaRegistro'),
    url(r'^regiter_pregunta/$', 'add_pregunta_view', name='vistaAddPregunta'),
    url(r'^regiter_pregunta_teoria/$', 'add_pregunta_teoria_view', name='vistaAddPreguntaTeoria'),
    #url(r'^regiter_pregunta_agilidad/$', 'add_pregunta_agilidad_view', name='vistaAddPreguntaAgilidad'),
    url(r'^add_pregunta_unica/$', 'add_pregunta_unica_view', name='vistaAddPreguntaTeoriaUnica'),
    url(r'^add_respuesta_unica/$', 'add_respuesta_unica_view', name='vistaAddRespuestaTeoriaUnica'),
    url(r'^add_pregunta_multiple/$', 'add_pregunta_multiple_view', name='vistaAddPreguntaTeoriaMultiple'),
    url(r'^add_respuesta_multiple/$', 'add_respuesta_multiple_view', name='vistaAddRespuestaTeoriaMultiple'),
    )