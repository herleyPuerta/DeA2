from django.conf.urls import patterns, url

urlpatterns = patterns('deados.apps.agility.views',
    url(r'^register_question_crafs_agility/$','add_pregunta_agilidad_dados_view', name='vistaAddPreguntaAgilidadDados'),
    url(r'^register_question_geometrics_agility/$','add_pregunta_agilidad_geometricas_view', name='vistaAddPreguntaAgilidadGeometricas'),
    url(r'^register_question_objects_agility/$','add_pregunta_agilidad_objetos_view', name='vistaAddPreguntaAgilidadObjetos'),
    url(r'^new_questions_agility/$', 'new_questions_agility_view', name='vistaNewQuestionAgility'),
	url(r'^add_images/$', 'add_images_view', name='vista_nuevas_imagenes'),
	url(r'^preguntas/agilidad/page/(?P<pagina>.*)/$', 'preguntas_agilidad_view', name='vistaPreguntasAgilidad'),
	#url(r'^edit_pregunta_agilidad/$', 'edit_agilidad_view', name='vistaEditAgilidadPregunta'),
	url(r'^edit/pregunta/agilidad/(?P<id_pregunta>.*)/$','edit_agilidad_view',name='vista_edit_agilidad'),
	url(r'^edit/respuesta/agilidad/$', 'edit_agilidad_respuesta_view', name='vista_edit_respuesta_agilidad'),
	url(r'^edit/respuesta/agilidad/dados/$', 'edit_agilidad_respuesta_dados_view', name='vista_edit_respuesta_agilidad_dados'),
	url(r'^edit/respuesta/agilidad/geometricas/$', 'edit_agilidad_respuesta_geometricas_view', name='vista_edit_respuesta_agilidad_geometricas'),
	url(r'^edit/respuesta/agilidad/objetos/$', 'edit_agilidad_respuesta_objetos_view', name='vista_edit_respuesta_agilidad_objetos'),
	url(r'^delete/pregunta/agilidad/(?P<id_pregunta>.*)/$', 'delete_agilidad_pregunta_view', name='vista_delete_pregunta_agilidad'),
)