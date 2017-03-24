from django.conf.urls import include, url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'), # index is name of html
    url(r'^logout/$', views.logout_view, name='logout'),  
    url(r'^about/$', views.about, name='about'),   
    
    #FBV
#     url(r'^meal/$', views.meal_list, name='meal_list'),
#     url(r'^meal/create/$', views.meal_create, name='meal_create'),
#     url(r'^meal/detail/(?P<pk>[0-9]+)$', views.meal_detail, name='meal_detail'),
#     url(r'^meal/update/(?P<pk>[0-9]+)$', views.meal_update, name='meal_update'),
#     url(r'^meal/delete/(?P<pk>[0-9]+)$', views.meal_delete, name='meal_delete'), 
    #CBV   
    url(r'^meal/$', views.MealList.as_view(), name='meal_list'),
    url(r'^meal/create$', views.MealCreate.as_view(), name='meal_create'),
    url(r'^meal/detail/(?P<pk>[0-9]+)$', views.MealDetail.as_view(), name='meal_detail'),
    url(r'^meal/update/(?P<pk>[0-9]+)$', views.MealUpdate.as_view(), name='meal_update'),
    url(r'^meal/delete/(?P<pk>[0-9]+)$', views.MealDelete.as_view(), name='meal_delete'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
    url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
    
]
