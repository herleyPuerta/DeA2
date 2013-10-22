from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion, Institucion_nombre
from deados.apps.home.forms import RegisterInstitucionForm

def index_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return HttpResponseRedirect('/registrar_institucion_name')
		return HttpResponseRedirect('/home')
	else:
		return HttpResponseRedirect('/login')
		

def home_view(request):
	return render_to_response('home.html',locals(),context_instance=RequestContext(request))


def add_pregunta_view(request):
	return render_to_response('formulario_pregunta.html',locals(),context_instance=RequestContext(request))

def add_pregunta_teoria_view(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			categoria = "teoria"
			tipoRespuesta = request.POST['tipoRespuesta']

		return render_to_response('pregunta_teoria.html',locals(),context_instance=RequestContext(request))


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

def logout_view(request):
	logout(request)
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
	if request.method == "POST":
		nombre = request.POST['nombre']
		institucion_nombre = Institucion_nombre(nombre=nombre)
		institucion_nombre.save()
		return render_to_response('nombre_succes.html',locals(),context_instance=RequestContext(request))
	else:
		return render_to_response('register_institucion_name.html',locals(),context_instance=RequestContext(request))

"""
def register_institucion_view(request):
	form = RegisterInstitucionForm()
	if request.method == "POST":
		form = RegisterInstitucionForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,password=password_one)
			u.save()
			return render_to_response('succes_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return 	render_to_response('registro.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('registro.html',ctx,context_instance=RequestContext(request))
"""