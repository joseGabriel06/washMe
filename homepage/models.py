from __future__ import unicode_literals
import calendar
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import utc
from washer.models import Register

class City(models.Model):
	name_city = models.CharField(max_length=50)


	def __str__(self):
		return self.name_city


class Packages(models.Model):
	name_packages = models.CharField(max_length=50)
	value         = models.CharField(max_length=50)

	def __str__(self):
		return self.name_packages



class Service(models.Model):
	hours         = models.ForeignKey(Packages,verbose_name='Horas',max_length=50)
	ciudad        = models.ForeignKey(City,verbose_name='Ciudad',max_length=50)
	nombre        = models.CharField(max_length=50)
	email         = models.CharField(max_length=50)
	celular       = models.CharField(max_length=50)
	fecha         = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
	timestamp     = models.DateTimeField(auto_now_add=True)
	owner         = models.ForeignKey(User, null=True, blank=True)


	

	class Meta:
		ordering = ['-timestamp']
	def __str__(self):
	 	return str(self.celular)

	def get_absolute_url(self):
		view_name = "detail"
		return reverse(view_name, kwargs={"pk": self.id})

