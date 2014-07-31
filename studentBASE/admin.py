from django.contrib import admin
from studentBASE.models import *
from django import forms

# Register your models here.
class StudentInline(admin.TabularInline):
	model = Student
	extra = 3

class GroupAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(GroupAdminForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
		#self.fields['base_rate'].queryset = Rate.objects.filter(company=self.instance.company)
		self.fields['cheif'].queryset = Student.objects.filter(group=self.instance.id)

class GroupAdmin(admin.ModelAdmin):
	inlines = [StudentInline]
	form = GroupAdminForm

class SignalAdmin(admin.ModelAdmin):
	list_display  = ('sender', 'type_signal', 'date')

admin.site.register(Group, GroupAdmin)
admin.site.register(Signal, SignalAdmin)
