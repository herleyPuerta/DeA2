from deados.apps.home.models import Institucion, Pregunta, Imagen, Respuesta_Agilidad
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.views.decorators.csrf import csrf_exempt

def preguntas_agilidad_view(request,pagina):
	if request.user.is_authenticated():
		institucion = request.user
		idInstitucion = Institucion.objects.get(user=institucion)
		preguntas_agilidad = Pregunta.objects.filter(idInstitucion=idInstitucion,categoria=2)
		paginator = Paginator(preguntas_agilidad,25) #cantidad de preguntas por pagina
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			preguntas = paginator.page(page)
		except (EmptyPage,InvalidPage):
			preguntas = paginator.page(paginator.num_pages)
		ctx = {'preguntas_agilidad':preguntas,'usuario':request.user}
		return render_to_response('agility/preguntas_agilidad.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def new_questions_agility_view(request):
	if request.user.is_authenticated():
		return render_to_response('agility/new_question_agility.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

@csrf_exempt
def add_pregunta_agilidad_dados_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 2
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta1 = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=5)
			pregunta1.save()
			imagenes = Imagen.objects.all()
			idpregunta = pregunta1.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			agilidad = request.POST['agilidad']
			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"

			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=determinacion1,contenido=contenido1,no_secuencia=1,tipo_imagen="Dados")
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen2,determinacion=determinacion2,contenido=contenido2,no_secuencia=2,tipo_imagen="Dados")
			respuesta2.save()

			respuesta3 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen3,determinacion=determinacion3,contenido=contenido3,no_secuencia=3,tipo_imagen="Dados")
			respuesta3.save()

			respuesta4 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen4,determinacion=determinacion4,contenido=contenido4,no_secuencia=4,tipo_imagen="Dados")
			respuesta4.save()

			respuesta5 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen5,determinacion=determinacion5,contenido=contenido5,no_secuencia=5,tipo_imagen="Dados")
			respuesta5.save()

			respuesta6 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen6,determinacion=determinacion6,contenido=contenido6,no_secuencia=6,tipo_imagen="Dados")
			respuesta6.save()
			print "respuesta guardada"
			return HttpResponse('True')
			#return render_to_response('pregunta_agilidad.html',locals(),context_instance=RequestContext(request))
		else:
			imagenes_dados = Imagen.objects.filter(tipo="Dados")
			return render_to_response('agility/pregunta_agilidad_dados.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


@csrf_exempt
def add_pregunta_agilidad_geometricas_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 2
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta1 = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=5)
			pregunta1.save()
			imagenes = Imagen.objects.all()
			idpregunta = pregunta1.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			agilidad = request.POST['agilidad']
			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"

			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=determinacion1,contenido=contenido1,no_secuencia=1,tipo_imagen="geometricas")
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen2,determinacion=determinacion2,contenido=contenido2,no_secuencia=2,tipo_imagen="geometricas")
			respuesta2.save()

			respuesta3 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen3,determinacion=determinacion3,contenido=contenido3,no_secuencia=3,tipo_imagen="geometricas")
			respuesta3.save()

			respuesta4 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen4,determinacion=determinacion4,contenido=contenido4,no_secuencia=4,tipo_imagen="geometricas")
			respuesta4.save()

			respuesta5 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen5,determinacion=determinacion5,contenido=contenido5,no_secuencia=5,tipo_imagen="geometricas")
			respuesta5.save()

			respuesta6 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen6,determinacion=determinacion6,contenido=contenido6,no_secuencia=6,tipo_imagen="geometricas")
			respuesta6.save()
			print "respuesta guardada"
			return HttpResponse('True')
			#return render_to_response('pregunta_agilidad.html',locals(),context_instance=RequestContext(request))
		else:
			imagenes_geometricas = Imagen.objects.filter(tipo="geometricas")
			return render_to_response('agility/pregunta_agilidad_geometricas.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


@csrf_exempt
def add_pregunta_agilidad_objetos_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 2
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta1 = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=5)
			pregunta1.save()
			imagenes = Imagen.objects.all()
			idpregunta = pregunta1.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			agilidad = request.POST['agilidad']
			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"

			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=determinacion1,contenido=contenido1,no_secuencia=1,tipo_imagen="objetos")
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen2,determinacion=determinacion2,contenido=contenido2,no_secuencia=2,tipo_imagen="objetos")
			respuesta2.save()

			respuesta3 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen3,determinacion=determinacion3,contenido=contenido3,no_secuencia=3,tipo_imagen="objetos")
			respuesta3.save()

			respuesta4 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen4,determinacion=determinacion4,contenido=contenido4,no_secuencia=4,tipo_imagen="objetos")
			respuesta4.save()

			respuesta5 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen5,determinacion=determinacion5,contenido=contenido5,no_secuencia=5,tipo_imagen="objetos")
			respuesta5.save()

			respuesta6 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen6,determinacion=determinacion6,contenido=contenido6,no_secuencia=6,tipo_imagen="objetos")
			respuesta6.save()
			print "respuesta guardada"
			return HttpResponse('True')
		else:
			imagenes_objetos = Imagen.objects.filter(tipo="objetos")
			return render_to_response('agility/pregunta_agilidad_objetos.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_images_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			for afile in request.FILES.getlist('archivo'):
				archivo = afile
				content_type = afile.content_type
				tipoPost = request.POST['tipo']
				if tipoPost == "1":
					tipo = "Dados"
				elif tipoPost == "2":
					tipo = "geometricas"
				else:
					tipo = "objetos"
				imagen = Imagen(archivo=archivo,content_type=content_type,tipo=tipo)
				imagen.save()
			return HttpResponseRedirect('/admin')
		else:
			return render_to_response('agility/imagenes.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def edit_agilidad_view(request,id_pregunta):
	if request.user.is_authenticated():
		pregunta = Pregunta.objects.get(id=id_pregunta)
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			contenido = request.POST['contenido']
			grado = request.POST['grado']
			categoria = 2
			tipoRespuesta = 5

			pregunta.idInstitucion = idInstitucion
			pregunta.contenido = contenido
			pregunta.grado = grado
			pregunta.categoria = categoria
			pregunta.tipoRespuesta = tipoRespuesta
			pregunta.save()
			respuesta1 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=1)
			respuesta2 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=2)
			respuesta3 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=3)
			respuesta4 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=4)
			respuesta5 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=5)
			respuesta6 = Respuesta_Agilidad.objects.get(idpregunta=id_pregunta,no_secuencia=6)
			if respuesta1.tipo_imagen == "Dados":
				imagenes_dados = Imagen.objects.filter(tipo="Dados")
				return render_to_response('agility/edit_answer_agility_crafs.html',locals(),context_instance=RequestContext(request))
			elif respuesta1.tipo_imagen == "geometricas":
				imagenes_geometricas = Imagen.objects.filter(tipo="geometricas")
				return render_to_response('agility/edit_answer_agility_geometrics.html',locals(),context_instance=RequestContext(request))
			else:
				imagenes_objetos = Imagen.objects.filter(tipo="objetos")
				return render_to_response('agility/edit_answer_agility_objects.html',locals(),context_instance=RequestContext(request))
		else:
			if pregunta.grado == 1:
				grados = "primaria"
			elif pregunta.grado == 2:
				grados = "sexto y septimo"
			else:
				grados = "octavo y noveno"
			return render_to_response('agility/edit_question_agility.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
		

@csrf_exempt
def edit_agilidad_respuesta_dados_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			print idpregunta
			pregunta = Pregunta.objects.get(id=idpregunta)
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			id5 = request.POST['id5']
			id6 = request.POST['id6']
			agilidad = request.POST['agilidad']

			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"
			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad.objects.get(id=id1)
			respuesta1.idpregunta = pregunta
			respuesta1.imagen = imagen1
			respuesta1.determinacion = determinacion1
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.tipo_imagen = "Dados"
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad.objects.get(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.imagen = imagen2
			respuesta2.determinacion = determinacion2
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.tipo_imagen = "Dados"
			respuesta2.save()


			respuesta3 = Respuesta_Agilidad.objects.get(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.imagen = imagen3
			respuesta3.determinacion = determinacion3
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.tipo_imagen = "Dados"
			respuesta3.save()


			respuesta4 = Respuesta_Agilidad.objects.get(id=id4)
			respuesta4.idpregunta = pregunta
			respuesta4.imagen = imagen4
			respuesta4.determinacion = determinacion4
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.tipo_imagen = "Dados"
			respuesta4.save()


			respuesta5 = Respuesta_Agilidad.objects.get(id=id5)
			respuesta5.idpregunta = pregunta
			respuesta5.imagen = imagen5
			respuesta5.determinacion = determinacion5
			respuesta5.contenido = contenido5
			respuesta5.no_secuencia = 5
			respuesta5.tipo_imagen = "Dados"
			respuesta5.save()


			respuesta6 = Respuesta_Agilidad.objects.get(id=id6)
			respuesta6.idpregunta = pregunta
			respuesta6.imagen = imagen6
			respuesta6.determinacion = determinacion6
			respuesta6.contenido = contenido6
			respuesta6.no_secuencia = 6
			respuesta6.tipo_imagen = "Dados"
			respuesta6.save()
			return HttpResponse('Respuesta guardada')
		else:
			return render_to_response('agility/edit_answer_agility_crafs.html',locals(),context_instance=RequestContext(request))


@csrf_exempt
def edit_agilidad_respuesta_geometricas_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			print idpregunta
			pregunta = Pregunta.objects.get(id=idpregunta)
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			id5 = request.POST['id5']
			id6 = request.POST['id6']
			agilidad = request.POST['agilidad']

			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"
			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad.objects.get(id=id1)
			respuesta1.idpregunta = pregunta
			respuesta1.imagen = imagen1
			respuesta1.determinacion = determinacion1
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.tipo_imagen = "geometricas"
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad.objects.get(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.imagen = imagen2
			respuesta2.determinacion = determinacion2
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.tipo_imagen = "geometricas"
			respuesta2.save()


			respuesta3 = Respuesta_Agilidad.objects.get(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.imagen = imagen3
			respuesta3.determinacion = determinacion3
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.tipo_imagen = "geometricas"
			respuesta3.save()


			respuesta4 = Respuesta_Agilidad.objects.get(id=id4)
			respuesta4.idpregunta = pregunta
			respuesta4.imagen = imagen4
			respuesta4.determinacion = determinacion4
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.tipo_imagen = "geometricas"
			respuesta4.save()


			respuesta5 = Respuesta_Agilidad.objects.get(id=id5)
			respuesta5.idpregunta = pregunta
			respuesta5.imagen = imagen5
			respuesta5.determinacion = determinacion5
			respuesta5.contenido = contenido5
			respuesta5.no_secuencia = 5
			respuesta5.tipo_imagen = "geometricas"
			respuesta5.save()


			respuesta6 = Respuesta_Agilidad.objects.get(id=id6)
			respuesta6.idpregunta = pregunta
			respuesta6.imagen = imagen6
			respuesta6.determinacion = determinacion6
			respuesta6.contenido = contenido6
			respuesta6.no_secuencia = 6
			respuesta6.tipo_imagen = "geometricas"
			respuesta6.save()
			return HttpResponse('Respuesta guardada')
		else:
			return render_to_response('agility/edit_answer_agility_geometrics.html',locals(),context_instance=RequestContext(request))


@csrf_exempt
def edit_agilidad_respuesta_objetos_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			print idpregunta
			pregunta = Pregunta.objects.get(id=idpregunta)
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			id5 = request.POST['id5']
			id6 = request.POST['id6']
			agilidad = request.POST['agilidad']

			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"
			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"

			respuesta1 = Respuesta_Agilidad.objects.get(id=id1)
			respuesta1.idpregunta = pregunta
			respuesta1.imagen = imagen1
			respuesta1.determinacion = determinacion1
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.tipo_imagen = "objetos"
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad.objects.get(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.imagen = imagen2
			respuesta2.determinacion = determinacion2
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.tipo_imagen = "objetos"
			respuesta2.save()


			respuesta3 = Respuesta_Agilidad.objects.get(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.imagen = imagen3
			respuesta3.determinacion = determinacion3
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.tipo_imagen = "objetos"
			respuesta3.save()


			respuesta4 = Respuesta_Agilidad.objects.get(id=id4)
			respuesta4.idpregunta = pregunta
			respuesta4.imagen = imagen4
			respuesta4.determinacion = determinacion4
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.tipo_imagen = "objetos"
			respuesta4.save()


			respuesta5 = Respuesta_Agilidad.objects.get(id=id5)
			respuesta5.idpregunta = pregunta
			respuesta5.imagen = imagen5
			respuesta5.determinacion = determinacion5
			respuesta5.contenido = contenido5
			respuesta5.no_secuencia = 5
			respuesta5.tipo_imagen = "objetos"
			respuesta5.save()


			respuesta6 = Respuesta_Agilidad.objects.get(id=id6)
			respuesta6.idpregunta = pregunta
			respuesta6.imagen = imagen6
			respuesta6.determinacion = determinacion6
			respuesta6.contenido = contenido6
			respuesta6.no_secuencia = 6
			respuesta6.tipo_imagen = "objetos"
			respuesta6.save()
			return HttpResponse('Respuesta guardada')
		else:
			return render_to_response('agility/edit_answer_agility_geometrics.html',locals(),context_instance=RequestContext(request))




@csrf_exempt
def edit_agilidad_respuesta_view(request):
	if request.user.is_authenticated():
		dados = 0
		geometricas = 0
		objetos = 0 
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			imagen_edit_type = request.POST['imagen_edit_type']
			if imagen_edit_type == "crafs":
				tipo_imagen = "Dados"
				dados = 1
			elif imagen_edit_type == "geometrics":
				tipo_imagen = "geometricas"
				geometricas = 1
			else:
				tipo_imagen = "objetos"
				objetos = 1
			agilidad = request.POST['agilidad']
			if agilidad == "1":
				determinacion1 = True
				contenido1 = "verdadero"
			else:
				determinacion1 = False
				contenido1 = "falso"

			if agilidad == "2":
				determinacion2 = True
				contenido2 = "verdadero"
			else:
				determinacion2 = False
				contenido2 = "falso"

			if agilidad == "3":
				determinacion3 = True
				contenido3 = "verdadero"
			else:
				determinacion3 = False
				contenido3 = "falso"

			if agilidad == "4":
				determinacion4 = True
				contenido4 = "verdadero"
			else:
				determinacion4 = False
				contenido4 = "falso"

			if agilidad == "5":
				determinacion5 = True
				contenido5 = "verdadero"
			else:
				determinacion5 = False
				contenido5 = "falso"

			if agilidad == "6":
				determinacion6 = True
				contenido6 = "verdadero"
			else:
				determinacion6 = False
				contenido6 = "falso"

			imagen1 = request.FILES['imagen1']
			imagen1.name = "imagen1"

			imagen2 = request.FILES['imagen2']
			imagen2.name = "imagen2"

			imagen3 = request.FILES['imagen3']
			imagen3.name = "imagen3"
			
			imagen4 = request.FILES['imagen4']
			imagen4.name = "imagen4"

			imagen5 = request.FILES['imagen5']
			imagen5.name = "imagen5"

			imagen6 = request.FILES['imagen6']
			imagen6.name = "imagen6"
			
			#respuesta1 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=determinacion1,contenido=contenido1,no_secuencia=1)

			respuesta1 = Respuesta_Agilidad.objects.get(id=id1)
			respuesta1.idpregunta = pregunta
			respuesta1.imagen = imagen1
			respuesta1.determinacion = determinacion1
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.tipo_imagen = tipo_imagen
			respuesta1.save()

			respuesta2 = Respuesta_Agilidad.objects.get(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.imagen = imagen2
			respuesta2.determinacion = determinacion2
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.tipo_imagen = tipo_imagen
			respuesta2.save()


			respuesta3 = Respuesta_Agilidad.objects.get(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.imagen = imagen3
			respuesta3.determinacion = determinacion3
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.tipo_imagen = tipo_imagen
			respuesta3.save()


			respuesta4 = Respuesta_Agilidad.objects.get(id=id4)
			respuesta4.idpregunta = pregunta
			respuesta4.imagen = imagen4
			respuesta4.determinacion = determinacion4
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.tipo_imagen = tipo_imagen
			respuesta4.save()


			respuesta5 = Respuesta_Agilidad.objects.get(id=id5)
			respuesta5.idpregunta = pregunta
			respuesta5.imagen = imagen5
			respuesta5.determinacion = determinacion5
			respuesta5.contenido = contenido5
			respuesta5.no_secuencia = 5
			respuesta5.tipo_imagen = tipo_imagen
			respuesta5.save()


			respuesta6 = Respuesta_Agilidad.objects.get(id=id6)
			respuesta6.idpregunta = pregunta
			respuesta6.imagen = imagen6
			respuesta6.determinacion = determinacion6
			respuesta6.contenido = contenido6
			respuesta6.no_secuencia = 6
			respuesta6.tipo_imagen = tipo_imagen
			respuesta6.save()
			return HttpResponse('Respuesta guardada')
		else:
			if dados == 1:
				#return render_to_response('agility/edit_answer_agility.html',locals(),context_instance=RequestContext(request))
				return render_to_response('agility/edit_answer_agility_crafs.html',locals(),context_instance=RequestContext(request))
			elif geometricas == 1:
				return render_to_response('agility/edit_answer_agility_geometrics.html',locals(),context_instance=RequestContext(request))
			elif objetos == 1:
				return render_to_response('agility/edit_answer_agility_objects.html',locals(),context_instance=RequestContext(request))
			return HttpResponse('a guardar')
	else:
		return HttpResponseRedirect('/')

def delete_agilidad_pregunta_view(request,id_pregunta):
	try:
		pregunta = Pregunta.objects.get(id = id_pregunta)
		pregunta.delete()
	except Pregunta.DoesNotExist:
		return HttpResponseRedirect("/")
	return HttpResponseRedirect("/preguntas/agilidad/page/1/")