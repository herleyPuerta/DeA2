from django.contrib import admin
from deados.apps.home.models import Institucion, Jugador, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion_nombre

class Respuesta_Multiple_Admin(admin.ModelAdmin):
	list_display = ('idPregunta','contenido','determinacion')
	search = ['contenido']

class Respuesta_Unica_Admin(admin.ModelAdmin):
	list_display = ('idPregunta','contenido','determinacion')
	search = ['contenido']

admin.site.register(Institucion)
admin.site.register(Jugador)
admin.site.register(Pregunta)
admin.site.register(Respuesta_Unica,Respuesta_Unica_Admin)
admin.site.register(Respuesta_Multiple,Respuesta_Multiple_Admin)
admin.site.register(Respuesta_Secuencial)
admin.site.register(Respuesta_Booleana)
admin.site.register(Institucion_nombre)