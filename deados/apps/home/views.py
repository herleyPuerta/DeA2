from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion, Institucion_nombre
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.views.decorators.csrf import csrf_exempt
import json

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
		return render_to_response('home/login.html',ctx, context_instance=RequestContext(request))
		

def home_view(request):
	if request.user.is_authenticated():
		if request.user.get_profile():
			user = request.user
			usuario = Institucion.objects.get(user=user)
			return render_to_response('home/home.html',locals(),context_instance=RequestContext(request))
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
			return render_to_response('home/bug_contrasenas.html',locals(),context_instance=RequestContext(request))
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			usuario 	 = User.objects.create_user(username=username,password=password)
			usuario.save()
			usua 	= authenticate(username=username,password=password)
			login(request,usua)
			perfil = Institucion(user=request.user)
			perfil.save()
			return render_to_response('home/succes_register.html',locals(),context_instance=RequestContext(request))
		return render_to_response('home/user_existente.html',locals(),context_instance=RequestContext(request))
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('password no coinciden')
	else:
		instituciones = Institucion_nombre.objects.all()
		return render_to_response('home/datosInstitucion.html',locals(),context_instance=RequestContext(request))
		

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')