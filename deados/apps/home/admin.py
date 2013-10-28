from django.contrib import admin
from deados.apps.home.models import Institucion, Jugador, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion_nombre

class Respuesta_Multiple_Admin(admin.ModelAdmin):
	list_display = ('idPregunta','contenido','determinacion')
	search = ['contenido']

class Respuesta_Unica_Admin(admin.ModelAdmin):
	list_display = ('id','idPregunta','contenido','determinacion','no_secuencia')
	search = ['contenido']

class Respuesta_Secuencial_Admin(admin.ModelAdmin):
	list_display = ('idPregunta','contenido','secuencia')

class Respuesta_Booleana_Admin(admin.ModelAdmin):
	list_display = ('idPregunta','determinacion')

class Pregunta_Admin(admin.ModelAdmin):
	list_display = ('contenido','tipoRespuesta')

admin.site.register(Institucion)
admin.site.register(Jugador)
admin.site.register(Pregunta,Pregunta_Admin)
admin.site.register(Respuesta_Unica,Respuesta_Unica_Admin)
admin.site.register(Respuesta_Multiple,Respuesta_Multiple_Admin)
admin.site.register(Respuesta_Secuencial,Respuesta_Secuencial_Admin)
admin.site.register(Respuesta_Booleana,Respuesta_Booleana_Admin)
admin.site.register(Institucion_nombre)