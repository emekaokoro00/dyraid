from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from braces import views # Ajax Mixin included
from rest_framework import generics

from .models import UserLog
from .forms import UserLogForm
from .serializers import UserLogSerializer
from django.template.context_processors import request

# Create your views here.

    
class UserLogList(LoginRequiredMixin, views.JSONResponseMixin, views.AjaxResponseMixin,
                  generic.ListView):
    model = UserLog
    context_object_name = 'userlog_list' 
    paginate_by = 2
    def get_ajax(self, request, *args, **kwargs):
        search_comment = self.request.GET.get('search_comment') 
        # data = request.GET.items() # form data        
        # userlog_list = UserLog.objects.all().filter(comment__icontains=search_comment)
        json_dict = {
            'comment': search_comment,
        }
        # Check packagins as json and interpreting json on html
        return self.render_json_response(json_dict)
    def get_queryset(self):
        userlog_list = super(UserLogList, self).get_queryset()
        userlog_list = userlog_list.filter(user=self.request.user)
        search_comment = self.request.GET.get('search_comment')
        if search_comment:
            userlog_list = userlog_list.filter(comment__icontains=search_comment)
        return userlog_list
    def get_context_data(self, **kwargs):
        #The current context.
        context = super(UserLogList, self).get_context_data(**kwargs)
        return context


class UserLogList_API(generics.ListCreateAPIView):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer
    
class UserLogDetail_API(generics.RetrieveUpdateDestroyAPIView): 
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer

# @login_required
# def search_userlog(request):
#     if request.GET:
#         if request.is_ajax():
#             print "AJAX"
#         else:
#             print "No AJAX"
#     
#         print request.GET
#     context = {'userlog_list':userlog_list}
#     return render(request,"home/userlog_list.html", context)
     
class UserLogCreate(LoginRequiredMixin, CreateView):
    model = UserLog
    form_class = UserLogForm
    def form_valid(self, form):
        form.instance.user = self.request.user #This is to populate user field with the currently logged on user
        return super(UserLogCreate, self).form_valid(form)
    
class UserLogDetail(LoginRequiredMixin, DetailView):
    model = UserLog
    form_class = UserLogForm
    template_name_suffix = '_detail'
     
class UserLogUpdate(LoginRequiredMixin, UpdateView):
    model = UserLog
    form_class = UserLogForm
    template_name_suffix = '_update_form'
     
class UserLogDelete(LoginRequiredMixin, DeleteView):
    model = UserLog
    success_url = reverse_lazy('userlog:userlog_list')