from django.db import models

SEX_CHOICES = (
    ('F', 'Mujer',),
    ('M', 'Hombre',),
    ('U', 'Otro',),
)

class Register(models.Model):
	first_name = models.CharField(max_length=30, verbose_name='Nombre')
	last_name  = models.CharField(max_length=30, verbose_name='Apellidos' )
	emiil      = models.EmailField(max_length=70,blank=True,verbose_name='Correo')
	phone      = models.CharField(max_length=30, verbose_name='Celular' )
	birthday   = models.DateField(verbose_name='Fecha de nacimiento')
	#image      = models.FileField(upload_to='image/%Y/%m/%d')
	status 	   = models.BooleanField()
	working    = models.BooleanField()
	sex        = models.CharField(max_length=1,choices=SEX_CHOICES,verbose_name='Género')
	timestamp  = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.first_name
