from django.conf.urls import include, url

from . import views

app_name = 'meal'
urlpatterns = [   
    
    #FBV
#     url(r'^meal/$', views.meal_list, name='meal_list'),
#     url(r'^meal/create/$', views.meal_create, name='meal_create'),
#     url(r'^meal/detail/(?P<pk>[0-9]+)$', views.meal_detail, name='meal_detail'),
#     url(r'^meal/update/(?P<pk>[0-9]+)$', views.meal_update, name='meal_update'),
#     url(r'^meal/delete/(?P<pk>[0-9]+)$', views.meal_delete, name='meal_delete'), 
    #CBV   
    url(r'^$', views.MealList.as_view(), name='meal_list'),
    url(r'^create$', views.MealCreate.as_view(), name='meal_create'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.MealDetail.as_view(), name='meal_detail'),
    url(r'^update/(?P<pk>[0-9]+)$', views.MealUpdate.as_view(), name='meal_update'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.MealDelete.as_view(), name='meal_delete'),
    
    # for browsable API with djangoRESTframework
    url(r'^api/$', views.MealList_API.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.MealDetail_API.as_view()),
]
