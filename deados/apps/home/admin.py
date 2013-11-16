from django.contrib import admin
from deados.apps.home.models import Institucion, Jugador, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion_nombre, Imagen, Respuesta_Agilidad

class Respuesta_Multiple_Admin(admin.ModelAdmin):
	list_display = ('idpregunta','contenido','determinacion')
	search = ['contenido']

class Respuesta_Unica_Admin(admin.ModelAdmin):
	list_display = ('id','idpregunta','contenido','determinacion','no_secuencia')
	search = ['contenido']

class Respuesta_Secuencial_Admin(admin.ModelAdmin):
	list_display = ('idpregunta','contenido','secuencia')

class Respuesta_Booleana_Admin(admin.ModelAdmin):
	list_display = ('id','idpregunta','determinacion','contenido')

class Respuesta_Agilidad_Admin(admin.ModelAdmin):
	list_display = ('id','idpregunta','determinacion','contenido','thumbnail')

class Pregunta_Admin(admin.ModelAdmin):
	list_display = ('id','contenido','tipoRespuesta')

class Imagen_admin(admin.ModelAdmin):
	list_display = ('id','tipo','content_type','thumbnail')


admin.site.register(Institucion)
admin.site.register(Jugador)
admin.site.register(Pregunta,Pregunta_Admin)
admin.site.register(Respuesta_Unica,Respuesta_Unica_Admin)
admin.site.register(Respuesta_Multiple,Respuesta_Multiple_Admin)
admin.site.register(Respuesta_Secuencial,Respuesta_Secuencial_Admin)
admin.site.register(Respuesta_Booleana,Respuesta_Booleana_Admin)
admin.site.register(Institucion_nombre)
admin.site.register(Imagen,Imagen_admin)
admin.site.register(Respuesta_Agilidad,Respuesta_Agilidad_Admin)