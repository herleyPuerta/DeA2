from django.db import models
from django.contrib.auth.models import User

class Institucion_nombre(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Institucion(models.Model):
	user = models.ForeignKey(User,related_name='perfil',unique=True)

	def __unicode__(self):
		return self.user.username

class Jugador(models.Model):
	identificacion   = models.CharField(max_length=30,unique=True)
	nombre			 = models.CharField(max_length=90)
	idInstitucion	 = models.ForeignKey(Institucion)
	puntos_totales	 = models.IntegerField()
	puntos_negativos = models.IntegerField()
	puntos_positivos = models.IntegerField()
	fechaRegistro 	 = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre
		

class Pregunta(models.Model):
	OPCIONES_GRADO		= ((1,'primaria'),(2,'sexto_septimo'),(3,'octavo_noveno'))
	OPCIONES_CATEGORIA	= ((1,'teoria'),(2,'agilidad_mental'))
	OPCIONES_RESPUESTA	= ((1,'unica_respuesta'),(2,'multiple_repuesta'),(3,'booleana'),(4,'secuencial'),(5,'agilidad_mental'))
	idInstitucion		= models.ForeignKey(Institucion)
	contenido			= models.CharField(max_length=61)
	grado    			= models.IntegerField(choices=OPCIONES_GRADO, default=1)
	categoria			= models.IntegerField(choices=OPCIONES_CATEGORIA,default=1)
	tipoRespuesta		= models.IntegerField(choices=OPCIONES_RESPUESTA,default=1)
	fechaRegistro 	    = models.DateField(auto_now_add=True)

	def get_answers_unicas(self):
		return Respuesta_Unica.objects.filter(idpregunta=self)

	def get_answers_multiples(self):
		return Respuesta_Multiple.objects.filter(idpregunta=self)

	def get_answers_booleanas(self):
		return Respuesta_Booleana.objects.filter(idpregunta=self)

	def get_answers_secuenciales(self):
		return Respuesta_Secuencial.objects.filter(idpregunta=self)

	def get_answers_agilidad(self):
		return Respuesta_Agilidad.objects.filter(idpregunta=self)

	def __unicode__(self):
		return self.contenido

class Respuesta(models.Model):
	idpregunta	 = models.ForeignKey(Pregunta)
	contenido	 = models.CharField(max_length=41)
	no_secuencia = models.IntegerField()

	class Meta:
		abstract = True

class Respuesta_Unica(Respuesta):
	determinacion = models.BooleanField(default=False)

	def __unicode__(self):
		#return u"%s (%s)" % (self.contenido, u", ".join([idpregunta.contenido for idpregunta in self.idpregunta.all()]))
		return self.contenido

class Respuesta_Multiple(Respuesta):
	determinacion = models.BooleanField(default=False)
	def __unicode__(self):
		return self.contenido

class Respuesta_Secuencial(Respuesta):
	secuencia = models.IntegerField()

	def __unicode__(self):
		return self.contenido

class Respuesta_Booleana(models.Model):
	idpregunta	  = models.ForeignKey(Pregunta)
	contenido 	  = models.CharField(max_length=41)
	determinacion = models.BooleanField(default=False)

	def __unicode__(self):
		return self.contenido

class Respuesta_Agilidad(models.Model):
	def url(self,filename):
		return "images/respuestas/%s/%s"%(self.idpregunta.id,filename)

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True

	idpregunta 	  = models.ForeignKey(Pregunta)
	imagen 		  = models.ImageField(upload_to=url)
	determinacion = models.BooleanField(default=False)
	contenido     = models.CharField(max_length=41) 
	no_secuencia  = models.IntegerField()
	tipo_imagen   = models.CharField(max_length=30)

	def __unicode__(self):
		return self.contenido


class Imagen(models.Model):

	def url(self,filename):
		return "images/agilidad_mental/%s"%(filename)

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.archivo,self.archivo)

	thumbnail.allow_tags = True

	archivo  	 = models.ImageField(upload_to=url)
	tipo 	     = models.CharField(max_length=60)
	content_type = models.CharField(max_length=40)

	def __unicode__(self):
		return self.tipo