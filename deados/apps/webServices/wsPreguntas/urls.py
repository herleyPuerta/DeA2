from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.webServices.wsPreguntas.views',
    url(r'^ws/instituciones/$', 'wsInstituciones_view', name='ws_instituciones_url'),
    url(r'^ws/preguntas_unicas/$', 'wsPreguntas_Unicas_view', name='ws_preguntas_unicas_url'),
    url(r'^ws/preguntas_multiples/$', 'wsPreguntas_Multiples_view', name='ws_preguntas_multiples_url'),
    url(r'^ws/preguntas_booleanas/$', 'wsPreguntas_Booleanas_view', name='ws_preguntas_booleanas_url'),
    url(r'^ws/preguntas_secuenciales/$', 'wsPregunas_Secuenciales_view', name='ws_preguntas_secuenciales_url'),
    url(r'^ws/preguntas_agilidad/$', 'wsPreguntas_Agilidad_view', name='ws_preguntas_agilidad_url'),

    url(r'^register_player/$', 'register_player_view', name='vista_regitrar_jugador'),
    url(r'^login_player/$', 'login_player_view', name='vista_ingresar_jugador'),
    url(r'^points_to_player/$', 'register_points_player', name='vista_ingresar_puntos'),
)