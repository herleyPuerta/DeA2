from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion, Institucion_nombre, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana
from deados.apps.home.forms import RegisterInstitucionForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/home')
	else:
		return HttpResponseRedirect('/login')


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			usuario = authenticate(username=username,password=password)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				if request.user.is_staff:
					return HttpResponseRedirect('/admin')
				else:
					return HttpResponseRedirect('/')
			else:
				mensaje = "usuario y/o password incorrecto"
		instituciones = Institucion_nombre.objects.all()
		ctx = {'mensaje':mensaje,'instituciones':instituciones}
		return render_to_response('login.html',ctx, context_instance=RequestContext(request))
		

def home_view(request):
	if request.user.is_authenticated():
		if request.user.get_profile():
			user = request.user
			usuario = Institucion.objects.get(user=user)
			return render_to_response('home.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_pregunta_view(request):
	if request.user.is_authenticated():
		return render_to_response('formulario_pregunta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def add_pregunta_teoria_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			categoria = "teoria"
			tipoRespuesta = request.POST['tipoRespuesta']
			if tipoRespuesta == "unica_respuesta":
				return HttpResponseRedirect('/add_pregunta_unica')
			elif tipoRespuesta == "multiple_repuesta":
				return HttpResponseRedirect('/add_pregunta_multiple')
			elif tipoRespuesta == "booleana":
				return HttpResponseRedirect('/add_pregunta_booleana')
			elif tipoRespuesta == "secuencial":
				return HttpResponseRedirect('/add_pregunta_secuencial')
			else:
				return render_to_response('pregunta_teoria.html',locals(),context_instance=RequestContext(request))
		return render_to_response('pregunta_teoria.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_pregunta_unica_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 1
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=1)
			pregunta.save()
			#guardar las respuestas
			idpregunta = pregunta.id
			pregunta = Pregunta.objects.get(id=idpregunta)

			unica = request.POST['unica']
			contenido1 = request.POST['respuesta1']
			if unica == "1":
				determinacion1 = True
			else:
				determinacion1 = False
			respuesta1 = Respuesta_Unica(idPregunta=pregunta,no_secuencia=1,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			if unica == "2":
				determinacion2 = True
			else:
				determinacion2 = False
			respuesta2 = Respuesta_Unica(idPregunta=pregunta,no_secuencia=2,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			if unica == "3":
				determinacion3 = True
			else:
				determinacion3 = False
			respuesta3 = Respuesta_Unica(idPregunta=pregunta,no_secuencia=3,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			if unica == "4":
				determinacion4 = True
			else:
				determinacion4 = False
			respuesta4 = Respuesta_Unica(idPregunta=pregunta,no_secuencia=4,contenido=contenido4,determinacion=determinacion4)
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_unica.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_pregunta_multiple_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 1
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=2)
			pregunta.save()
			#guardar las respuestas.
			idpregunta = pregunta.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			try:
				if request.POST['multiple1']:
					determinacion1 = True
			except:
				determinacion1 = False

			try:
				if request.POST['multiple2']:
					determinacion2 = True
			except:
				determinacion2 = False

			try:
				if request.POST['multiple3']:
					determinacion3 = True
			except:
				determinacion3 = False

			try:
				if request.POST['multiple4']:
					determinacion4 = True
			except:
				determinacion4 = False

			contenido1 = request.POST['respuesta1']
			respuesta1 = Respuesta_Multiple(idPregunta=pregunta,no_secuencia=1,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			respuesta2 = Respuesta_Multiple(idPregunta=pregunta,no_secuencia=2,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			respuesta3 = Respuesta_Multiple(idPregunta=pregunta,no_secuencia=3,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			respuesta4 = Respuesta_Multiple(idPregunta=pregunta,no_secuencia=4,contenido=contenido4,determinacion=determinacion4)
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_multiple.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_pregunta_secuencial_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 1
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=4)
			pregunta.save()
			#guardar las respuestas.
			idpregunta = pregunta.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			contenido1 = request.POST['respuesta1']
			contenido2 = request.POST['respuesta2']
			contenido3 = request.POST['respuesta3']
			contenido4 = request.POST['respuesta4']
			secuencia1 = request.POST['secuencia1']
			secuencia2 = request.POST['secuencia2']
			secuencia3 = request.POST['secuencia3']
			secuencia4 = request.POST['secuencia4']
			respuesta1 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=1,contenido=contenido1,secuencia=secuencia1)
			respuesta1.save()
			respuesta2 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=2,contenido=contenido2,secuencia=secuencia2)
			respuesta2.save()
			respuesta3 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=3,contenido=contenido3,secuencia=secuencia3)
			respuesta3.save()
			respuesta4 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=4,contenido=contenido4,secuencia=secuencia4)
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_secuencial.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_pregunta_booleana_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 1
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=3)
			pregunta.save()
			#guardar las respuestas.
			idpregunta = pregunta.id
			pregunta = Pregunta.objects.get(id=idpregunta)
			booleana = request.POST['booleana']
			if booleana == "1":
				determinacion = True
				contenido = "verdadero"
			else:
				determinacion = True
				contenido = "falso"
			respuesta = Respuesta_Booleana(idPregunta=pregunta,determinacion=determinacion,contenido=contenido)
			respuesta.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_booleana.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def register_institucion_view(request):
	if request.method == "POST":
		username = request.POST['nombre']
		password = request.POST['password_one']
		password_two = request.POST['password_two']
		if password == password_two:
			pass
		else:
			return render_to_response('bug_contrasenas.html',locals(),context_instance=RequestContext(request))
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			usuario 	 = User.objects.create_user(username=username,password=password)
			usuario.save()
			usua 	= authenticate(username=username,password=password)
			login(request,usua)
			perfil = Institucion(user=request.user)
			perfil.save()
			return render_to_response('succes_register.html',locals(),context_instance=RequestContext(request))
		return render_to_response('user_existente.html',locals(),context_instance=RequestContext(request))
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('password no coinciden')
	else:
		instituciones = Institucion_nombre.objects.all()
		return render_to_response('datosInstitucion.html',locals(),context_instance=RequestContext(request))

def preguntas_teoricas_view(request,pagina):
	if request.user.is_authenticated():
		institucion = request.user
		idInstitucion = Institucion.objects.get(user=institucion)
		preguntas_teoricas = Pregunta.objects.filter(idInstitucion=idInstitucion)
		paginator = Paginator(preguntas_teoricas,4) #cantidad de preguntas por pagina
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			preguntas = paginator.page(page)
		except (EmptyPage,InvalidPage):
			preguntas = paginator.page(paginator.num_pages)
		ctx = {'preguntas_teoricas':preguntas,'usuario':request.user}
		return render_to_response('preguntas_teoricas.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def edit_pregunta_teorica_view(request,id_pregunta):
	if request.user.is_authenticated():
		pregunta = Pregunta.objects.get(id=id_pregunta)
		if pregunta.grado == 1:
			grados = "primaria"
		elif pregunta.grado == 2:
			grados = "sexto y septimo"
		else:
			grados = "octavo y noveno"
		ctx = {'pregunta':pregunta,'grados':grados}
		if pregunta.tipoRespuesta == 1:
			return render_to_response('edit_unica_pregunta.html',ctx,context_instance=RequestContext(request))
		elif pregunta.tipoRespuesta == 2:
			return render_to_response('edit_multiple_pregunta.html',ctx,context_instance=RequestContext(request))
		elif pregunta.tipoRespuesta == 3:
			return render_to_response('edit_booleana_pregunta.html',ctx,context_instance=RequestContext(request))
		elif pregunta.tipoRespuesta == 4:
			return render_to_response('edit_secuencial_pregunta.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def edit_unica_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['id']
			pregunta = Pregunta.objects.get(id=idpregunta)
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			contenido = request.POST['contenido']
			grado = request.POST['grado']
			categoria = 1
			tipoRespuesta = 1

			pregunta.idInstitucion = idInstitucion
			pregunta.contenido = contenido
			pregunta.grado = grado
			pregunta.categoria = categoria
			pregunta.tipoRespuesta = tipoRespuesta
			pregunta.save()
			#editar las respuestas asociadas a las preguntas
			respuesta1 = Respuesta_Unica.objects.get(idPregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Unica.objects.get(idPregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Unica.objects.get(idPregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Unica.objects.get(idPregunta=idpregunta,no_secuencia=4)

			ctx = {'pregunta':pregunta,'respuesta1':respuesta1,'respuesta2':respuesta2,'respuesta3':respuesta3,'respuesta4':respuesta4}
			return render_to_response('edit_unica_respuesta.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('edit_unica_pregunta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def edit_unica_respuesta_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			unica = request.POST['unica']
			contenido1 = request.POST['respuesta1']
			if unica == "1":
				determinacion1 = True
			else:
				determinacion1 = False
			respuesta1 = Respuesta_Unica.objects.get(id=id1)
			respuesta1.idPregunta = pregunta
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.determinacion = determinacion1
			respuesta1.save()

			#respuesta 2
			contenido2 = request.POST['respuesta2']
			if unica == "2":
				determinacion2 = True
			else:
				determinacion2 = False
			respuesta2 = Respuesta_Unica.objects.get(id=id2)
			respuesta2.idPregunta = pregunta
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.determinacion = determinacion2
			respuesta2.save()

			#respuesta 3
			contenido3 = request.POST['respuesta3']
			if unica == "3":
				determinacion3 = True
			else:
				determinacion3 = False
			
			respuesta3 = Respuesta_Unica.objects.get(id=id3)
			respuesta3.idPregunta = pregunta
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.determinacion = determinacion3
			respuesta3.save()
			
			contenido4 = request.POST['respuesta4']
			if unica == "4":
				determinacion4 = True
			else:
				determinacion4 = False
			respuesta4 = Respuesta_Unica.objects.get(id=id4)
			respuesta4.idPregunta = pregunta
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.determinacion = determinacion4
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('edit_unica_respuesta.html',ctx,context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/')


def edit_multiple_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['id']
			pregunta = Pregunta.objects.get(id=idpregunta)
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			contenido = request.POST['contenido']
			grado = request.POST['grado']
			categoria = 1
			tipoRespuesta = 2

			pregunta.idInstitucion = idInstitucion
			pregunta.contenido = contenido
			pregunta.grado = grado
			pregunta.categoria = categoria
			pregunta.tipoRespuesta = tipoRespuesta
			pregunta.save()
			#editar las respuestas asociadas a las preguntas
			respuesta1 = Respuesta_Multiple.objects.get(idPregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Multiple.objects.get(idPregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Multiple.objects.get(idPregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Multiple.objects.get(idPregunta=idpregunta,no_secuencia=4)

			ctx = {'pregunta':pregunta,'respuesta1':respuesta1,'respuesta2':respuesta2,'respuesta3':respuesta3,'respuesta4':respuesta4}
			return render_to_response('edit_multiple_respuesta.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('edit_multiple_pregunta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def edit_multiple_respuesta_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			contenido1 = request.POST['respuesta1']
			try:
				if request.POST['multiple1']:
					determinacion1 = True
			except:
				determinacion1 = False

			try:
				if request.POST['multiple2']:
					determinacion2 = True
			except:
				determinacion2 = False

			try:
				if request.POST['multiple3']:
					determinacion3 = True
			except:
				determinacion3 = False

			try:
				if request.POST['multiple4']:
					determinacion4 = True
			except:
				determinacion4 = False

			respuesta1 = Respuesta_Multiple.objects.get(id=id1)
			respuesta1.idPregunta = pregunta
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.determinacion = determinacion1
			respuesta1.save()

			#respuesta 2
			contenido2 = request.POST['respuesta2']
			respuesta2 = Respuesta_Multiple.objects.get(id=id2)
			respuesta2.idPregunta = pregunta
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.determinacion = determinacion2
			respuesta2.save()

			#respuesta 3
			contenido3 = request.POST['respuesta3']			
			respuesta3 = Respuesta_Multiple.objects.get(id=id3)
			respuesta3.idPregunta = pregunta
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.determinacion = determinacion3
			respuesta3.save()
			
			contenido4 = request.POST['respuesta4']
			respuesta4 = Respuesta_Multiple.objects.get(id=id4)
			respuesta4.idPregunta = pregunta
			respuesta4.contenido = contenido4
			respuesta4.no_secuencia = 4
			respuesta4.determinacion = determinacion4
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('edit_multiple_respuesta.html',ctx,context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/')


def edit_secuencial_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['id']
			pregunta = Pregunta.objects.get(id=idpregunta)
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			contenido = request.POST['contenido']
			grado = request.POST['grado']
			categoria = 1
			tipoRespuesta = 4

			pregunta.idInstitucion = idInstitucion
			pregunta.contenido = contenido
			pregunta.grado = grado
			pregunta.categoria = categoria
			pregunta.tipoRespuesta = tipoRespuesta
			pregunta.save()
			#editar las respuestas asociadas a las preguntas
			respuesta1 = Respuesta_Secuencial.objects.get(idPregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Secuencial.objects.get(idPregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Secuencial.objects.get(idPregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Secuencial.objects.get(idPregunta=idpregunta,no_secuencia=4)

			ctx = {'pregunta':pregunta,'respuesta1':respuesta1,'respuesta2':respuesta2,'respuesta3':respuesta3,'respuesta4':respuesta4}
			return render_to_response('edit_secuencial_respuesta.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('edit_secuencial_pregunta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def edit_secuencial_respuesta_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			id1 = request.POST['id1']
			id2 = request.POST['id2']
			id3 = request.POST['id3']
			id4 = request.POST['id4']
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			#guardar las respuestas.
			contenido1 = request.POST['respuesta1']
			contenido2 = request.POST['respuesta2']
			contenido3 = request.POST['respuesta3']
			contenido4 = request.POST['respuesta4']
			secuencia1 = request.POST['secuencia1']
			secuencia2 = request.POST['secuencia2']
			secuencia3 = request.POST['secuencia3']
			secuencia4 = request.POST['secuencia4']
			#respuesta1 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=1,contenido=contenido1,secuencia=secuencia1)
			respuesta1 = Respuesta_Secuencial(id=id1)
			respuesta1.idPregunta = pregunta
			respuesta1.no_secuencia = 1
			respuesta1.contenido = contenido1
			respuesta1.secuencia = secuencia1	
			respuesta1.save()
			#respuesta2 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=2,contenido=contenido2,secuencia=secuencia2)
			respuesta2 = Respuesta_Secuencial(id=id2)
			respuesta2.idPregunta = pregunta
			respuesta2.no_secuencia = 2
			respuesta2.contenido = contenido2
			respuesta2.secuencia = secuencia2
			respuesta2.save()
			#respuesta3 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=3,contenido=contenido3,secuencia=secuencia3)
			respuesta3 = Respuesta_Secuencial(id=id3)
			respuesta3.idPregunta = pregunta
			respuesta3.no_secuencia = 3
			respuesta3.contenido = contenido3
			respuesta3.secuencia = secuencia3
			respuesta3.save()
			#respuesta4 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=4,contenido=contenido4,secuencia=secuencia4)
			respuesta4 = Respuesta_Secuencial(id=id4)
			respuesta4.idPregunta = pregunta
			respuesta4.no_secuencia = 4
			respuesta4.contenido = contenido4
			respuesta4.secuencia = secuencia4
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('edit_secuencial_respuesta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def edit_booleana_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['id']
			pregunta = Pregunta.objects.get(id=idpregunta)
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			contenido = request.POST['contenido']
			grado = request.POST['grado']
			categoria = 1
			tipoRespuesta = 3

			pregunta.idInstitucion = idInstitucion
			pregunta.contenido = contenido
			pregunta.grado = grado
			pregunta.categoria = categoria
			pregunta.tipoRespuesta = tipoRespuesta
			pregunta.save()
			#editar las respuestas asociadas a las preguntas
			respuesta = Respuesta_Booleana.objects.get(idPregunta=idpregunta)

			ctx = {'pregunta':pregunta,'respuesta':respuesta}
			return render_to_response('edit_booleana_respuesta.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('edit_booleana_pregunta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def edit_booleana_respuesta_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			id1 = request.POST['id1']
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			#guardar las respuestas.
			booleana = request.POST['booleana']
			#respuesta1 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=1,contenido=contenido1,secuencia=secuencia1)
			respuesta = Respuesta_Booleana(id=id1)
			respuesta.idPregunta = pregunta
			if booleana == "1":
				determinacion = True
				contenido = "verdadero"
			else:
				determinacion = True
				contenido = "falso"
			respuesta.determinacion = determinacion
			respuesta.contenido = contenido	
			respuesta.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('edit_booleana_respuesta.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def delete_pregunta_teorica_view(request,id_pregunta):
	try:
		pregunta = Pregunta.objects.get(id = id_pregunta)
		pregunta.delete()
	except Pregunta.DoesNotExist:
		return HttpResponseRedirect("/")
	return HttpResponseRedirect("/preguntas/teoricas/page/1/")


def del_logro_view(request, id_logro):
	try:
		logro = Logro.objects.get(idLogro = id_logro)
		logro.delete()
	except Logro.DoesNotExist:
		return HttpResponseRedirect("/")
	
	return HttpResponseRedirect("/")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@csrf_exempt
def new_event_view(request):
  json_data = request.read()
  eventoObj = json.loads(json_data)
  p_user = User.objects.get(username= eventoObj["Username"],email = eventoObj['Email'])
  listLugar = eventoObj['lugar']
  place = Place(address = listLugar[0], city = listLugar[1] , country = listLugar[2])
  evento = Event(creador = p_user, nombre = eventoObj["nombre"], descripcion = eventoObj["descripcion"], fecha_realizacion = eventoObj["fecha"], hora = eventoObj["hora"], privacidad = eventoObj["privacidad"], cantidad_invitados = eventoObj["cantidadinvitados"], aprobar_asistencia = eventoObj["aprobarasistencia"], tipo = eventoObj["tipoevento"], lugar = place)
  evento.save() 
  #return render_to_response('index.html',locals(),  context_instance=RequestContext(request))
  return HttpResponse("Evento creado con exitosamente")

def register_player_view(request):
	