from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.webServices.wsPreguntas.views',
    url(r'^ws/preguntas/$', 'wsPreguntas_view', name='ws_preguntas_url'),
    url(r'^ws/respuestas/unicas/$', 'wsRespuestas_Unicas_view', name='ws_respuestas_unicas_url'),
    url(r'^ws/respuestas/multiples/$', 'wsRespuestas_Multiples_view', name='ws_respuestas_multiples_url'),
    url(r'^ws/respuestas/booleanas/$', 'wsRespuestas_Booleanas_view', name='ws_respuestas_booleanas_url'),
    url(r'^ws/respuestas/secuenciales/$', 'wsRespuestas_Secuenciales_view', name='ws_respuestas_secuenciales_url'),
    url(r'^ws/instituciones/$', 'wsInstituciones_view', name='ws_instituciones_url'),

)