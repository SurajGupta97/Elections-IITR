from django.conf.urls import patterns ,url

from authentication import views 

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^logout/$',views.log_out,name='logout'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^profile/complete/$',views.profile_complete,name='profile_complete'),
	url(r'^profile/complete/submit/$',views.profile_complete_submit,),
	)

