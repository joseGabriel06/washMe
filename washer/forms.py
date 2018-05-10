from django import forms
from .models import Register
from django.conf import settings

class UploadForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ['first_name', 'emiil','sex']
	

	