from django.shortcuts import render
from django.views.generic.base import View
from studentBASE.models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import Context, RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(StudentList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		#context['student_list'] = Student.objects.all()
		context['show_group_name'] = True
		return context

class GroupDetailView(DetailView):
	model = Group
	context_object_name = 'group'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(GroupDetailView, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		group = get_object_or_404(Group, id=self.kwargs['pk'])
		context['group'] = group
		context['student_list'] = group.student_set.all()
		return context

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
		if 'group_id' in request.GET:
			group_id = request.GET['group_id']
			group = Group.objects.get(id=group_id)
			variables = RequestContext(request, {
				'group' : group,
			})
		else:
			variables = RequestContext(request, {})
		return render(request, self.template_name, variables)

class StudentUpdate(UpdateView):
	model = Student

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(StudentUpdate, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		group_list = Group.objects.all()
		context['group_list'] = group_list
		return context

class StudentDelete(DeleteView):
	model = Student
	success_url = "/group/"

class StudentDetailView(DetailView):
	model = Student
	context_object_name = 'student'

	def get_object(self):
		return get_object_or_404(Student, id=self.kwargs['pk'])


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def login(request):
	if 'username' in request.POST and request.POST['username']:
		u = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=u, password=password)
		if user is not None and user.is_active:
			# Правильный пароль и пользователь "активен"
			auth.login(request, user)
			# Перенаправление на "правильную" страницу
			return HttpResponseRedirect("/")
		else:
			# Отображение страницы с ошибкой
			return HttpResponseRedirect("/login")
    
	return render(request, 'registration/login.html')