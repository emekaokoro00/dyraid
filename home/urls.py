from django.conf.urls import include, url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),     
    
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
    
    url(r'^userlog/$', views.UserLogList.as_view(), name='userlog_list'),
    url(r'^userlog/create$', views.UserLogCreate.as_view(), name='userlog_create'),
    url(r'^userlog/detail/(?P<pk>[0-9]+)$', views.UserLogDetail.as_view(), name='userlog_detail'),
    url(r'^userlog/update/(?P<pk>[0-9]+)$', views.UserLogUpdate.as_view(), name='userlog_update'),
    url(r'^userlog/delete/(?P<pk>[0-9]+)$', views.UserLogDelete.as_view(), name='userlog_delete'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
    url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
#     url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
]
