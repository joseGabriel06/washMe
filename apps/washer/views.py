import os
from apps.washer.forms import UploadForm
from apps.washer.models import Register
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect 
from material import (
    Layout, Fieldset, Row, Column, Span, Field,
    Span2, Span3, Span4, Span5, Span6, Span7,
    Span8, Span9, Span10, Span11, Span12,
    LayoutMixin)

class NewWasherView(CreateView):
    model = Register
    form_class = UploadForm
    def form_valid(self, form):
        form.instance.status  = False
        form.instance.working = False
        dir          = os.path.join(settings.BASE_DIR, "templates" , "email_washer.html" )
        archivo      = open( dir , "r")
        contenido    = archivo.read()
        first_name   = form.instance.first_name
        last_name    = form.instance.last_name
        emiil        = form.instance.emiil
        contenido    = contenido.format(first_name,last_name)
        subject      = 'washme'
        text_content = 'Mensaje...nLinea 2nLinea3'
        html_content = contenido
        from_email   = '"origen" <Hola@wioclean.com>'
        to           = emiil
        msg          = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super(NewWasherView, self).form_valid(form)
    def get_form(self):
        form = super(NewWasherView, self).get_form(self.form_class)
        form.fields['birthday'].widget.attrs.update({'class': 'datepicker'})
        return form
    def get_success_url(self):
        return reverse('done')
    layout = Layout(
        Row('first_name','last_name'),
        Row('emiil','phone'),
        Row('birthday','sex')
    )
    
class HomeDoneView(TemplateView):
    template_name = "washer/done.html"
    
class WasherListView(ListView):
    model = Register
    def get_queryset(self, *args, **kwargs):
        qs = super(WasherListView,self).get_queryset(*args,**kwargs)
        return qs
