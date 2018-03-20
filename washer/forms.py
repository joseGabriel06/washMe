from django import forms
from .models import Register

class UploadForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ['first_name', 'last_name', 'emiil', 'phone','birthday','sex']
