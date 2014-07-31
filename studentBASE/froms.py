from django import forms
from django.views.generic import FormView

class CreateGroupForm(forms.Form):
	title = forms.CharField(max_length=50)
	cheif = forms.ForeignKey()


class CreateGroupFormView(FormView):
	form_class = CreateGroupForm
	template_name = 'studentBASE/create_group.html'
	success_url = 'success'