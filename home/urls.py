from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<meal_type_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<meal_type_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
    url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
]
