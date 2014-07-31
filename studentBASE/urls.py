from django.conf.urls import patterns, include, url
from studentBASE import views

urlpatterns = patterns('',
	url(r'^$', views.MainPage.as_view()),
	url(r'^group/$', views.GroupList.as_view(), name='group_list'),
	url(r'^group_view/(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group_detail'), 
	url(r'^group/add/$', views.GroupCreate.as_view(), name='group_add'),
	url(r'^group/(?P<pk>\d+)/$', views.GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<pk>\d+)/delete/$', views.GroupDelete.as_view(), name='group_delete'),
    url(r'^student/$', views.StudentList.as_view(), name='student_list'),
    url(r'^student/add/$', views.StudentCreate.as_view(), name='student_add'),
    url(r'^student_view/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student_detail'), 
    url(r'^student/(?P<pk>\d+)/delete/$', views.StudentDelete.as_view(), name='student_delete'),
    url(r'^student/(?P<pk>\d+)/$', views.StudentUpdate.as_view(), name='student_update'),
)