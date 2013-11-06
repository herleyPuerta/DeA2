from django.http import HttpResponse
from deados.apps.home.models import Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion
from django.contrib.auth.models import User
from django.core import serializers

def wsRespuestas_Unicas_view(request):
	data = serializers.serialize("json",Respuesta_Unica.objects.all())
	return HttpResponse(data,mimetype='application/json')

def wsRespuestas_Multiples_view(request):
	data = serializers.serialize("json",Respuesta_Multiple.objects.all())
	return HttpResponse(data,mimetype='application/json')

def wsRespuestas_Secuenciales_view(request):
	data = serializers.serialize("json",Respuesta_Secuencial.objects.all())
	return HttpResponse(data,mimetype='application/json')

def wsRespuestas_Booleanas_view(request):
	data = serializers.serialize("json",Respuesta_Booleana.objects.all())
	return HttpResponse(data,mimetype='application/json')


def wsPreguntas_view(request):
	data = serializers.serialize("json",Pregunta.objects.all())
	return HttpResponse(data,mimetype='application/json')

def wsInstituciones_view(request):
	data = serializers.serialize("json",User.objects.all())
	return HttpResponse(data,mimetype='application/json')
