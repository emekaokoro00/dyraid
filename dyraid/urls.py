"""dyraid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [        
    url(r'', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^userlog/', include('userlog.urls')),
    url(r'^meal/', include('meal.urls')),
    url(r'^admin/', admin.site.urls),
    
    # for browsable API with djangoRESTframework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # url(r'^accounts/', include('registration.backends.simple.urls')), #django-registration sets the user management page
    url(r'^accounts/', include('allauth.urls')), #django-allauth sets the user management page
    
    url(r'^login/', views.login, {'template_name': 'registration/login.html'}), # sets the login page
    # url(r'^logout/$', views.logout, {'next_page': 'login'}),  
    # url(r'^logout/$', views.logout, {'next_page': 'home/logout.html'}),  
]
