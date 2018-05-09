from django import forms
from .models import Register
from django.conf import settings

class UploadForm(forms.ModelForm):
	birthday = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='Fecha de nacimiento')
	class Meta:
		model = Register
		fields = ['first_name', 'last_name', 'emiil', 'phone','birthday','sex']
	



# class MyAddForm(forms.ModelForm):
#      thedate = forms.DateField(input_formats=('%d-%m-%Y'))

#      class Meta:
#          model = myModel
#          fields = ["thedate", ]
#          widgets = {
#               'thedate': forms.DateInput(format='%d-%m-%Y'),
#          }