from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion, Institucion_nombre, Pregunta, Respuesta_Unica, Respuesta_Multiple
from deados.apps.home.forms import RegisterInstitucionForm

def index_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return HttpResponseRedirect('/register_institucion_name')
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
					return HttpResponseRedirect('/')
				return HttpResponseRedirect('/')
			else:
				mensaje = "usuario y/o password incorrecto"
		instituciones = Institucion_nombre.objects.all()
		ctx = {'mensaje':mensaje,'instituciones':instituciones}
		return render_to_response('login.html',ctx, context_instance=RequestContext(request))
		

def home_view(request):
	if request.user.is_authenticated():
		return render_to_response('home.html',locals(),context_instance=RequestContext(request))


def add_pregunta_view(request):
	if request.user.is_authenticated():
		return render_to_response('formulario_pregunta.html',locals(),context_instance=RequestContext(request))

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
				return HttpResponseRedirect('/add_respuesta_booleana')
			elif tipoRespuesta == "secuencial":
				return HttpResponseRedirect('/add_respuesta_secuencial')
			else:
				return render_to_response('pregunta_teoria.html',locals(),context_instance=RequestContext(request))
		return render_to_response('pregunta_teoria.html',locals(),context_instance=RequestContext(request))


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
			ctx = {'pregunta':pregunta}
			return render_to_response('respuesta_unica.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_unica.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')


def add_respuesta_unica_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			numeroPregunta = request.POST['numeroPregunta']
			pregunta = Pregunta.objects.get(id=numeroPregunta)
			unica = request.POST['unica']
			contenido1 = request.POST['respuesta1']
			if unica == "1":
				determinacion1 = True
			else:
				determinacion1 = False
			respuesta1 = Respuesta_Unica(idPregunta=pregunta,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			if unica == "2":
				determinacion2 = True
			else:
				determinacion2 = False
			respuesta2 = Respuesta_Unica(idPregunta=pregunta,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			if unica == "3":
				determinacion3 = True
			else:
				determinacion3 = False
			respuesta3 = Respuesta_Unica(idPregunta=pregunta,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			if unica == "4":
				determinacion4 = True
			else:
				determinacion4 = False
			respuesta4 = Respuesta_Unica(idPregunta=pregunta,contenido=contenido4,determinacion=determinacion4)
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('respuesta_unica.html',locals(),context_instance=RequestContext(request))
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
			ctx = {'pregunta':pregunta}
			return render_to_response('respuesta_multiple.html',ctx,context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_unica.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def add_respuesta_multiple_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			numeroPregunta = request.POST['numeroPregunta']
			pregunta = Pregunta.objects.get(id=numeroPregunta)
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

			respuesta1 = Respuesta_Multiple(idPregunta=pregunta,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			respuesta2 = Respuesta_Multiple(idPregunta=pregunta,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			respuesta3 = Respuesta_Multiple(idPregunta=pregunta,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			respuesta4 = Respuesta_Multiple(idPregunta=pregunta,contenido=contenido4,determinacion=determinacion4)
			respuesta4.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('respuesta_multiple.html',locals(),context_instance=RequestContext(request))
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
			return render_to_response('nombre_succes.html',locals(),context_instance=RequestContext(request))
		return render_to_response('user_existente.html',locals(),context_instance=RequestContext(request))
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('password no coinciden')
	else:
		instituciones = Institucion_nombre.objects.all()
		return render_to_response('datosInstitucion.html',locals(),context_instance=RequestContext(request))


def register_institucion_name_view(request):
	if request.user.is_staff:
		if request.method == "POST":
			nombre = request.POST['nombre']
			institucion_nombre = Institucion_nombre(nombre=nombre)
			institucion_nombre.save()
			return render_to_response('nombre_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('register_institucion_name.html',locals(),context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')