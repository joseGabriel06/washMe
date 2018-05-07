from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Service
from .models import City
from .models import Packages

from washer.models import Register
from material import (
    Layout, Fieldset, Row, Column, Span, Field,
    Span2, Span3, Span4, Span5, Span6, Span7,
    Span8, Span9, Span10, Span11, Span12,
    LayoutMixin)

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class HomeView(TemplateView):
	template_name =  'homepage/home_view.pug'
	
def create_service(request):
	if request.method == 'POST':		
		hours  = request.POST['hours']
		ciudad = request.POST['ciudad']
		name   = request.POST['name']
		email  = request.POST['email']
		numero = request.POST['numero']
		date   = request.POST['date']
		
		hours  = Packages.objects.get(id=hours)
		ciudad   = City.objects.get(id=ciudad)

		Service.objects.create(
			 hours   = hours,
			 ciudad  = ciudad,
			 nombre  = name,
			 email   = email,
			 celular = numero,
			 fecha   = date,
			 owner   = request.user
		)
		return HttpResponse('')


class ServiceListView(LoginRequiredMixin,ListView):
	template_name  = 'homepage/home_pay_view.pug'
	model = Service
	def get_queryset(self, *args, **kwargs):
		qs = super(ServiceListView,self).get_queryset(*args,**kwargs).filter(owner=self.request.user)
		return qs
	
class TermPageView(TemplateView):

    template_name = "homepage/terminos.html"
