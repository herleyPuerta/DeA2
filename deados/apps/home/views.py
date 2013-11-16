from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion, Institucion_nombre, Pregunta, Respuesta_Unica, Respuesta_Multiple, Respuesta_Secuencial, Respuesta_Booleana, Jugador, Imagen, Respuesta_Agilidad
from deados.apps.home.forms import RegisterInstitucionForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
import base64
#from base64 import b64decode
from django.core.files.base import ContentFile

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

def add_pregunta_agilidad_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			institucion = request.user
			idInstitucion = Institucion.objects.get(user=institucion)
			categoria = 2
			grado = request.POST['grado']
			contenido  = request.POST['pregunta']
			pregunta = Pregunta(idInstitucion=idInstitucion,contenido=contenido,grado=grado,categoria=categoria,tipoRespuesta=5)
			pregunta.save()
			imagenes = Imagen.objects.all()
			rangos = range(1,6)
			return render_to_response('respuesta_agilidad.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('pregunta_agilidad.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)


@csrf_exempt
def add_respuesta_agilidad_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			imagen1 = request.FILES['imagen1']
			#image_data = decode_base64(imagen1)
			#image_data = base64.b64decode(imagen1)
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			#imagene = ContentFile(image_data, 'imagen1.png')
			#photo.image.save(name, ContentFile(buffer))
			respuesta = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=True,contenido="verdadero")
			#respuesta.idpregunta=pregunta
			#respuesta.imagen.save(image_data,ContentFile(buffer))
			respuesta.save()
			print "respuesta guardada"
			#print imgdata
			if(respuesta.save()):
				return HttpResponseRedirect('/')
		else:
			return render_to_response('respuesta_agilidad.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def translate_non_alphanumerics(to_translate, translate_to=u'_'):
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
    if isinstance(to_translate, unicode):
        translate_table = dict((ord(char), unicode(translate_to))
                               for char in not_letters_or_digits)
    else:
        assert isinstance(to_translate, str)
        translate_table = string.maketrans(not_letters_or_digits,
                                           translate_to
                                              *len(not_letters_or_digits))
    return to_translate.translate(translate_table)


"""
def add_respuesta_agilidad_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			idpregunta = request.POST['idpregunta']
			pregunta = Pregunta.objects.get(id=idpregunta)
			agilidad = request.POST['agilidad']
			if agilidad == "1":
				determinacion1 = True
				contenido1 = "Verdadero"
			else:
				determinacion1 = False
				contenido1 = "Falso"
			imagen1 = request.FILES['imagen1']
			respuesta1 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen1,determinacion=determinacion1,contenido=contenido1)
			respuesta1.save()
			if agilidad == "2":
				determinacion2 = True
				contenido2 = "Verdadero"
			else:
				determinacion2 = False
				contenido2 = "Falso"
			imagen2 = request.FILES['imagen2']
			respuesta2 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen2,determinacion=determinacion2,contenido=contenido2)
			respuesta2.save()
			if agilidad == "3":
				determinacion3 = True
				contenido3 = "Verdadero"
			else:
				determinacion3 = False
				contenido3 = "Falso"
			imagen3 = request.FILES['imagen3']
			respuesta3 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen3,determinacion=determinacion3,contenido=contenido3)
			respuesta3.save()
			if agilidad == "4":
				determinacion4 = True
				contenido4 = "Verdadero"
			else:
				determinacion4 = False
				contenido4 = "Falso"
			imagen4 = request.FILES['imagen4']
			respuesta4 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen4,determinacion=determinacion4,contenido=contenido4)
			respuesta4.save()
			if agilidad == "5":
				determinacion5 = True
				contenido5 = "Verdadero"
			else:
				determinacion5 = False
				contenido5 = "Falso"
			imagen5 = request.FILES['imagen5']
			respuesta5 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen5,determinacion=determinacion5,contenido=contenido5)
			respuesta5.save()
			if agilidad == "6":
				determinacion6 = True
				contenido6 = "Verdadero"
			else:
				determinacion6 = False
				contenido6 = "Falso"
			imagen6 = request.FILES['imagen6']
			respuesta6 = Respuesta_Agilidad(idpregunta=pregunta,imagen=imagen6,determinacion=determinacion6,contenido=contenido6)
			respuesta6.save()
			return render_to_response('pregunta_succes.html',locals(),context_instance=RequestContext(request))
		else:
			return render_to_response('respuesta_agilidad.html',locals(),context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
"""


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
			respuesta1 = Respuesta_Unica(idpregunta=pregunta,no_secuencia=1,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			if unica == "2":
				determinacion2 = True
			else:
				determinacion2 = False
			respuesta2 = Respuesta_Unica(idpregunta=pregunta,no_secuencia=2,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			if unica == "3":
				determinacion3 = True
			else:
				determinacion3 = False
			respuesta3 = Respuesta_Unica(idpregunta=pregunta,no_secuencia=3,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			if unica == "4":
				determinacion4 = True
			else:
				determinacion4 = False
			respuesta4 = Respuesta_Unica(idpregunta=pregunta,no_secuencia=4,contenido=contenido4,determinacion=determinacion4)
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
			respuesta1 = Respuesta_Multiple(idpregunta=pregunta,no_secuencia=1,contenido=contenido1,determinacion=determinacion1)
			respuesta1.save()
			contenido2 = request.POST['respuesta2']
			respuesta2 = Respuesta_Multiple(idpregunta=pregunta,no_secuencia=2,contenido=contenido2,determinacion=determinacion2)
			respuesta2.save()
			contenido3 = request.POST['respuesta3']
			respuesta3 = Respuesta_Multiple(idpregunta=pregunta,no_secuencia=3,contenido=contenido3,determinacion=determinacion3)
			respuesta3.save()
			contenido4 = request.POST['respuesta4']
			respuesta4 = Respuesta_Multiple(idpregunta=pregunta,no_secuencia=4,contenido=contenido4,determinacion=determinacion4)
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
			respuesta1 = Respuesta_Secuencial(idpregunta=pregunta,no_secuencia=1,contenido=contenido1,secuencia=secuencia1)
			respuesta1.save()
			respuesta2 = Respuesta_Secuencial(idpregunta=pregunta,no_secuencia=2,contenido=contenido2,secuencia=secuencia2)
			respuesta2.save()
			respuesta3 = Respuesta_Secuencial(idpregunta=pregunta,no_secuencia=3,contenido=contenido3,secuencia=secuencia3)
			respuesta3.save()
			respuesta4 = Respuesta_Secuencial(idpregunta=pregunta,no_secuencia=4,contenido=contenido4,secuencia=secuencia4)
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
			respuesta = Respuesta_Booleana(idpregunta=pregunta,determinacion=determinacion,contenido=contenido)
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
		preguntas_teoricas = Pregunta.objects.filter(idInstitucion=idInstitucion,categoria=1)
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
			respuesta1 = Respuesta_Unica.objects.get(idpregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Unica.objects.get(idpregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Unica.objects.get(idpregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Unica.objects.get(idpregunta=idpregunta,no_secuencia=4)

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
			respuesta1.idpregunta = pregunta
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
			respuesta2.idpregunta = pregunta
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
			respuesta3.idpregunta = pregunta
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
			respuesta4.idpregunta = pregunta
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
			respuesta1 = Respuesta_Multiple.objects.get(idpregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Multiple.objects.get(idpregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Multiple.objects.get(idpregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Multiple.objects.get(idpregunta=idpregunta,no_secuencia=4)

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
			respuesta1.idpregunta = pregunta
			respuesta1.contenido = contenido1
			respuesta1.no_secuencia = 1
			respuesta1.determinacion = determinacion1
			respuesta1.save()

			#respuesta 2
			contenido2 = request.POST['respuesta2']
			respuesta2 = Respuesta_Multiple.objects.get(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.contenido = contenido2
			respuesta2.no_secuencia = 2
			respuesta2.determinacion = determinacion2
			respuesta2.save()

			#respuesta 3
			contenido3 = request.POST['respuesta3']			
			respuesta3 = Respuesta_Multiple.objects.get(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.contenido = contenido3
			respuesta3.no_secuencia = 3
			respuesta3.determinacion = determinacion3
			respuesta3.save()
			
			contenido4 = request.POST['respuesta4']
			respuesta4 = Respuesta_Multiple.objects.get(id=id4)
			respuesta4.idpregunta = pregunta
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
			respuesta1 = Respuesta_Secuencial.objects.get(idpregunta=idpregunta,no_secuencia=1)
			respuesta2 = Respuesta_Secuencial.objects.get(idpregunta=idpregunta,no_secuencia=2)
			respuesta3 = Respuesta_Secuencial.objects.get(idpregunta=idpregunta,no_secuencia=3)
			respuesta4 = Respuesta_Secuencial.objects.get(idpregunta=idpregunta,no_secuencia=4)

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
			respuesta1.idpregunta = pregunta
			respuesta1.no_secuencia = 1
			respuesta1.contenido = contenido1
			respuesta1.secuencia = secuencia1	
			respuesta1.save()
			#respuesta2 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=2,contenido=contenido2,secuencia=secuencia2)
			respuesta2 = Respuesta_Secuencial(id=id2)
			respuesta2.idpregunta = pregunta
			respuesta2.no_secuencia = 2
			respuesta2.contenido = contenido2
			respuesta2.secuencia = secuencia2
			respuesta2.save()
			#respuesta3 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=3,contenido=contenido3,secuencia=secuencia3)
			respuesta3 = Respuesta_Secuencial(id=id3)
			respuesta3.idpregunta = pregunta
			respuesta3.no_secuencia = 3
			respuesta3.contenido = contenido3
			respuesta3.secuencia = secuencia3
			respuesta3.save()
			#respuesta4 = Respuesta_Secuencial(idPregunta=pregunta,no_secuencia=4,contenido=contenido4,secuencia=secuencia4)
			respuesta4 = Respuesta_Secuencial(id=id4)
			respuesta4.idpregunta = pregunta
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
			respuesta = Respuesta_Booleana.objects.get(idpregunta=idpregunta)

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
			respuesta.idpregunta = pregunta
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
def register_player_view(request):
	json_recibido = request.read()
	objetoJson = json.loads(json_recibido)
	idinstitucion = objetoJson['idinstitucion']
	username = objetoJson['username']
	identificacion = objetoJson['identificacion']
	institucion = Institucion.objects.get(id=idinstitucion)
	print idinstitucion
	print username
	print identificacion
	player = Jugador(nombre=username,identificacion=identificacion,idInstitucion=institucion,puntos_totales=0,puntos_negativos=0,puntos_positivos=0)
	player.save()
	return HttpResponse("True")

"""
def add_images_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			for afile in request.FILES.getlist('archivo'):
				archivo = afile
				content_type = afile.content_type
				imagen = Imagen(archivo=archivo,content_type=content_type,tipo=tipo)
				imagen.save()
			return HttpResponseRedirect('/')
		else:
			return render_to_response('imagenes.html',locals(),context_instance=RequestContext(request))
"""

	