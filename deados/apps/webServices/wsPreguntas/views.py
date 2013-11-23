from django.http import HttpResponse
from deados.apps.home.models import Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Institucion, Jugador
from django.contrib.auth.models import User
import json
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

@csrf_exempt
def register_player_view(request):
	json_recibido = request.read()
	print json_recibido
	objetoJson = json.loads(json_recibido)
	#.decode("utf-8-sig")
	idinstitucion = objetoJson['idinstitucion']
	username = objetoJson['username']
	identificacion = objetoJson['identificacion']
	institucion = Institucion.objects.get(id=idinstitucion)
	print idinstitucion
	print username
	print identificacion
	try:
		jugador = Jugador.objects.get(identificacion=identificacion)
		return HttpResponse('ya_existe')
	except Jugador.DoesNotExist:
		player = Jugador(nombre=username,identificacion=identificacion,idInstitucion=institucion,puntos_totales=0,puntos_negativos=0,puntos_positivos=0)
		player.save()
		return HttpResponse("guardado")


@csrf_exempt
def login_player_view(request):
	json_recibido = request.read()
	objetoJson = json.loads(json_recibido)
	identificacion = objetoJson['identificacion']
	print identificacion
	if Jugador.objects.filter(identificacion=identificacion):
		return HttpResponse('existe')
	else:
		return HttpResponse('no_existe')


@csrf_exempt
def register_points_player(request):
	json_recibido = request.read()
	objetoJson = json.loads(json_recibido)
	puntos_positivos = objetoJson['positivos']
	puntos_negativos = objetoJson['negativos']
	identificacion   = objetoJson['identificacion']
	print puntos_positivos
	print puntos_negativos
	print identificacion
	player = Jugador.objects.get(identificacion=identificacion)
	positivos_player = player.puntos_positivos
	negativos_player = player.puntos_negativos
	totales_postivos = positivos_player+puntos_positivos
	totales_negativos = negativos_player+puntos_negativos
	
	totales_to_player = totales_postivos+totales_negativos
	positivos_to_player = positivos_player+puntos_positivos
	negativos_to_player = negativos_player+puntos_negativos

	player.puntos_totales = totales_to_player
	player.puntos_negativos = negativos_to_player
	player.puntos_positivos = positivos_to_player
	try:
		player.save()
		return HttpResponse('puntos_registrados')
	except:
		return HttpResponse('puntos_no_registrados')