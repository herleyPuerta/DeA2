from django.http import HttpResponse
from deados.apps.home.models import Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion, Jugador
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


def wsPreguntas_Unicas_view(request):
	preguntas = Pregunta.objects.filter(tipoRespuesta=1)
	questions = list()
	for p in preguntas:
		r = p.get_answers_unicas()
		print r
		answers = list()
		for w in r:
			answers.append({"pk":w.id,"idpregunta":w.idpregunta.id,"determinacion":w.determinacion,"contenido":w.contenido})
		questions.append({
			"pk":p.id,
			"contenido":p.contenido,
			"grado":p.grado,
			"categoria":p.categoria,
			"tipoRespuesta":p.tipoRespuesta,
			"respuestas": answers
			})
	#print "LISTA",questions
	data = json.dumps(questions)
	#print "DATA:", data
	return HttpResponse(data,mimetype='application/json')


def wsPreguntas_Multiples_view(request):
	preguntas = Pregunta.objects.filter(tipoRespuesta=2)
	questions = list()
	for p in preguntas:
		r = p.get_answers_multiples()
		answers = list()
		for w in r:
			answers.append({"pk":w.id,"idpregunta":w.idpregunta.id,"determinacion":w.determinacion,"contenido":w.contenido})
		questions.append({
			"pk":p.id,
			"contenido":p.contenido,
			"grado":p.grado,
			"categoria":p.categoria,
			"tipoRespuesta":p.tipoRespuesta,
			"respuestas": answers
			})
	#print "LISTA",questions
	data = json.dumps(questions)
	#print "DATA:", data
	return HttpResponse(data,mimetype='application/json')


def wsPreguntas_Booleanas_view(request):
	preguntas = Pregunta.objects.filter(tipoRespuesta=3)
	questions = list()
	for p in preguntas:
		r = p.get_answers_booleanas()
		answers = list()
		for w in r:
			answers.append({"pk":w.id,"idpregunta":w.idpregunta.id,"determinacion":w.determinacion,"contenido":w.contenido})
		questions.append({
			"pk":p.id,
			"contenido":p.contenido,
			"grado":p.grado,
			"categoria":p.categoria,
			"tipoRespuesta":p.tipoRespuesta,
			"respuestas": answers
			})
	#print "LISTA",questions
	data = json.dumps(questions)
	#print "DATA:", data
	return HttpResponse(data,mimetype='application/json')


def wsPregunas_Secuenciales_view(request):
	preguntas = Pregunta.objects.filter(tipoRespuesta=4)
	questions = list()
	for p in preguntas:
		r = p.get_answers_secuenciales()
		answers = list()
		for w in r:
			answers.append({"pk":w.id,"idpregunta":w.idpregunta.id,"secuencia":w.secuencia,"contenido":w.contenido})
		questions.append({
			"pk":p.id,
			"contenido":p.contenido,
			"grado":p.grado,
			"categoria":p.categoria,
			"tipoRespuesta":p.tipoRespuesta,
			"respuestas": answers
			})
	#print "LISTA",questions
	data = json.dumps(questions)
	#print "DATA:", data
	return HttpResponse(data,mimetype='application/json')

def wsPreguntas_Agilidad_view(request):
	preguntas = Pregunta.objects.filter(tipoRespuesta=5)
	questions = list()
	for p in preguntas:
		r = p.get_answers_agilidad()
		answers = list()
		for w in r:
			answers.append({"pk":w.id,"idpregunta":w.idpregunta.id,"imagen":w.imagen.url,"determinacion":w.determinacion,"contenido":w.contenido})
		questions.append({
			"pk":p.id,
			"contenido":p.contenido,
			"grado":p.grado,
			"categoria":p.categoria,
			"tipoRespuesta":p.tipoRespuesta,
			"respuestas": answers
			})
	#print "LISTA",questions
	data = json.dumps(questions)
	#print "DATA:", data
	return HttpResponse(data,mimetype='application/json')


def wsInstituciones_view(request):
	users = User.objects.all()
	instituciones = Institucion.objects.all()
	usr = list()
	for i in instituciones:
		for u in users:
			if i.user.id == u.id:
				usr.append({"idinstitucion":i.id,"username":u.username})
	data = json.dumps(usr)
	return HttpResponse(data,mimetype="application/json")