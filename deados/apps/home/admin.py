from django.contrib import admin
from deados.apps.home.models import Institucion, Jugador, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion_nombre

admin.site.register(Institucion)
admin.site.register(Jugador)
admin.site.register(Pregunta)
admin.site.register(Respuesta_Unica)
admin.site.register(Respuesta_Multiple)
admin.site.register(Respuesta_Secuencial)
admin.site.register(Respuesta_Booleana)
admin.site.register(Institucion_nombre)