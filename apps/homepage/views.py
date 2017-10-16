from django.shortcuts import render
from django.core.serializers import serialize
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.conf import settings
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
from .Forms import ServiceForm

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class Detail(DetailView):
	template_name = 'homepage/service_detail.pug'
	model = Service

class ServiceListView(ListView):
	template_name  = 'homepage/service_list.pug'
	model = Service
	def get_queryset(self, *args, **kwargs):
		qs = super(ServiceListView,self).get_queryset(*args,**kwargs)
		return qs

class NewServiceView(CreateView):
	template_name = 'homepage/service_form.pug'
	form_class = ServiceForm
	def get_success_url(self):
		return reverse('home')

class SeviceUpdateView(UpdateView):
	template_name = 'homepage/service_form.pug'
	model = Service
	form_class = ServiceForm

class ServiceDeleteView(DeleteView):
	template_name = 'homepage/service_confirm_delete.pug'
	model = Service
	def get_success_url(self):
		return reverse('home')


# @login_required(login_url="/accounts/login/?next=/")
# def new_service_view(request):
# 	titulo="Nuevo Servicio"
# 	form =  LogServiceForm(request.POST or None)
# 	if form.is_valid():
# 		form_data = form.cleaned_data
# 		hou =form_data.get('hours')
# 		dat =form_data.get('date_delivery')
# 		tim =form_data.get('time_entry')
# 		die =form_data.get('direction')
# 		obj = LogServiceForm.objects.create(hours=hou, date_delivery=dat, time_entry=tim, direction=die)

# template_name='service.pug'

# 	context = {
# 		"el_form":form,
# 		"titulo":titulo
# 	}
# 	return render(request,"loggame_form.pug",context)

	
# @login_required(login_url="/accounts/login/?next=/")
# def func_games(request):
#     games = serialize("json",LogGame.objects.all())
#     return HttpResponse(games, content_type="application/json")

# class ClassHistoryTemplateView(LoginRequiredMixin, TemplateView):
# 	template_name = "history.pug"
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(ClassHistoryTemplateView, self).get_context_data(*args,**kwargs)
# 		context["titulo"]='Hola Mundo'
# 		return context


# @login_required(login_url="/accounts/login/?next=/")
# def func_get_users(request):
# 	users = serialize("json",User.objects.all())
# 	return HttpResponse(users, content_type="application/json")
	