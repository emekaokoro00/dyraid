from django.conf.urls import include, url

from . import views
from .views import UserViewSet
from rest_framework import routers
from django.contrib.auth.models import User
    
app_name = 'home'

# Routers provide an easy way of automatically determining URL conf
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'), # index is name of html
    url(r'^logout/$', views.logout_view, name='logout'),  
    url(r'^about/$', views.about, name='about'),   
    
    # for browsable API with djangoRESTframework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<meal_type_id>[0-9]+)/increase_calorie_for_meal/$', views.increase_calorie_for_meal, name='increase_calorie_for_meal'),
    url(r'^(?P<logger_id>[0-9]+)/rate/$', views.rate, name='rate'),
    
]
