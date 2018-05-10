from django.contrib import admin
from .models  import Register

class AdminWaseher(admin.ModelAdmin):
	list_display   = ['first_name','emiil', 'status', 'working']
	list_filter    = ['sex', 'status','working']
	search_fields  = ['first_name']
	#list_editable = ['status', 'working']
	class Meta:
		model = Register

admin.site.register(Register,AdminWaseher)
