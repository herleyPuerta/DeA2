from django.db import models

class Imagen(models.Model):
	def url(self,filename):
		return "images/agilidad/%s/%s"%(self.id,filename)
	archivo = models.ImageField(upload_to=url)
	descripcion = models.CharField(max_length=40)

	def __unicode__(self):
		return self.descripcion
