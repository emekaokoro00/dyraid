from django.conf.urls import include, url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'), # index is name of html
    url(r'^logout/$', views.logout_view, name='logout'),  
    url(r'^about/$', views.about, name='about'),   
    
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
    url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
    
]
