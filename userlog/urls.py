from django.conf.urls import include, url

from . import views

app_name = 'userlog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^logout/$', views.logout_view, name='logout'),     
    
    url(r'^$', views.UserLogList.as_view(), name='userlog_list'),
    # url(r'^userlog/$', views.UserLogList.as_view(), name='userlog_list'),
    url(r'^create$', views.UserLogCreate.as_view(), name='userlog_create'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.UserLogDetail.as_view(), name='userlog_detail'),
    url(r'^update/(?P<pk>[0-9]+)$', views.UserLogUpdate.as_view(), name='userlog_update'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.UserLogDelete.as_view(), name='userlog_delete'),
    # url(r'^userlog/$', views.search_userlog, name='search_userlog'),
    
    # api for json
    url(r'^api/$', views.UserLogList_API.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.UserLogDetail_API.as_view()),
]
