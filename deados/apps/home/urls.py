from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
    url(r'^login/$', 'login_view', name='vistaLogin'),
    url(r'^logout/$', 'logout_view', name='vistaLogout'),
    url(r'^home/$', 'home_view', name='vistaHome'),
    url(r'^register_institucion/$', 'register_institucion_view', name='vistaRegistro'),
    url(r'^regiter_pregunta/$', 'add_pregunta_view', name='vistaAddPregunta'),
    url(r'^regiter_pregunta_teoria/$', 'add_pregunta_teoria_view', name='vistaAddPreguntaTeoria'),
    #url(r'^regiter_pregunta_agilidad/$', 'add_pregunta_agilidad_view', name='vistaAddPreguntaAgilidad'),
    url(r'^add_pregunta_unica/$', 'add_pregunta_unica_view', name='vistaAddPreguntaTeoriaUnica'),
    url(r'^add_pregunta_multiple/$', 'add_pregunta_multiple_view', name='vistaAddPreguntaTeoriaMultiple'),
    url(r'^add_pregunta_secuencial/$', 'add_pregunta_secuencial_view', name='vistaAddPreguntaTeoriaSecuencial'),
    url(r'^add_pregunta_booleana/$', 'add_pregunta_booleana_view', name='vistaAddPreguntaTeoriaBooleana'),
    url(r'^preguntas/teoricas/$', 'preguntas_teoricas_view', name='vistaPreguntasTeoricas'),

    url(r'^edit/pregunta/teorica/(?P<id_pregunta>.*)/$','edit_pregunta_teorica_view',name='vista_edit_teoria'),
    
    url(r'^edit_pregunta_unica/$', 'edit_unica_view', name='vistaEditTeoriaUnicaPregunta'),
    url(r'^edit_respuesta_unica/$', 'edit_unica_respuesta_view', name='vistaEditTeoriaUnicaRespuesta'),

    url(r'^edit_pregunta_multiple/$', 'edit_multiple_view', name='vistaEditTeoriaMultiplePregunta'),
    url(r'^edit_respuesta_multiple/$', 'edit_multiple_respuesta_view', name='vistaEditTeoriaMultipleRespuesta'),

    url(r'^edit_pregunta_secuencial/$', 'edit_secuencial_view', name='vistaEditTeoriaSecuencialPregunta'),
    url(r'^edit_respuesta_secuencial/$', 'edit_secuencial_respuesta_view', name='vistaEditTeoriaSecuencialRespuesta'),

    url(r'^edit_pregunta_booleana/$', 'edit_booleana_view', name='vistaEditTeoriaBooleanaPregunta'),
    url(r'^edit_respuesta_booleana/$', 'edit_booleana_respuesta_view', name='vistaEditTeoriaBooleanaRespuesta'),

    url(r'^delete/pregunta/teorica/(?P<id_pregunta>.*)/$','delete_pregunta_teorica_view',name='vista_delete_teoria'),
    )