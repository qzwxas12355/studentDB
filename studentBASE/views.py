from django.shortcuts import render
from django.views.generic.base import View
from studentBASE.models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import Context, RequestContext

# Create your views here.

class MainPage(View):
	template_name = 'studentBASE/main.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class GroupList(ListView):
	model = Group
	context_object_name = 'group_list'
	template_name = 'studentBASE/group_list.html'
'''
	def get(self, request, *args, **kwargs):
		group_list = Group.objects.all()
		return render(request, self.template_name, {'group_list': group_list})
'''
class StudentList(ListView):
	model = Student
	context_object_name = 'student_list'

class GroupDetailView(DetailView):
	model = Group
	context_object_name = 'group'

	def get_object(self):
		return get_object_or_404(Group, id=self.kwargs['pk'])

class GroupCreate(CreateView):
	model = Group

class GroupUpdate(UpdateView):
	model = Group

class GroupDelete(DeleteView):
	model = Group
	success_url = reverse_lazy('group_list')

class StudentCreate(CreateView):
	model = Student
	template_name = 'studentBASE/student_form_custom.html'

	def get(self, request, *args, **kwargs):
		group_id = request.GET['group_id']
		group = Group.objects.get(id=group_id)
		variables = RequestContext(request, {
			'group' : group,
			})
		return render(request, self.template_name, variables)

class StudentUpdate(UpdateView):
	model = Student

class StudentDelete(DeleteView):
	model = Student
	success_url = "/group/"

class StudentDetailView(DetailView):
	model = Student
	context_object_name = 'student'

	def get_object(self):
		return get_object_or_404(Student, id=self.kwargs['pk'])