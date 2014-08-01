import os
from django.conf.urls import patterns, include, url
from studentBASE import views
from django.contrib.auth.decorators import login_required


static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
	#url(r'^$', views.MainPage.as_view(), name='index'),
	url(r'^group/$', views.GroupList.as_view(), name='group_list'),
    url(r'^$', views.GroupList.as_view(), name='index'),
	url(r'^group_view/(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group_detail'), 
	url(r'^group/add/$', login_required(views.GroupCreate.as_view()), name='group_add'),
	url(r'^group/(?P<pk>\d+)/$', login_required(views.GroupUpdate.as_view()), name='group_update'),
    url(r'^group/(?P<pk>\d+)/delete/$', login_required(views.GroupDelete.as_view()), name='group_delete'),
    url(r'^student/$', views.StudentList.as_view(), name='student_list'),
    url(r'^student/add/$', login_required(views.StudentCreate.as_view()), name='student_add'),
    url(r'^student_view/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student_detail'), 
    url(r'^student/(?P<pk>\d+)/delete/$', login_required(views.StudentDelete.as_view()), name='student_delete'),
    url(r'^student/(?P<pk>\d+)/$', login_required(views.StudentUpdate.as_view()), name='student_update'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static}),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
)