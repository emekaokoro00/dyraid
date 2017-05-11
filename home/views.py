from django.shortcuts import render, get_object_or_404, redirect, _get_queryset
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.forms.models import ModelForm

from braces import views # Ajax Mixin included

from meal.models import Meal, Meal_Type
from meal.forms import MealForm
from userlog.models import UserLog
from .forms import UserForm

#REST
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

from userlog.views import UserLogList

# Create your views here.

#NOTES
#Currently you use the admin login
#You can create your own login ... check "https://docs.djangoproject.com/en/1.10/topics/auth/default/"
@login_required() # settings for redirect found in settings.py - LOGIN_URL
def index(request):
#     latest_meal_type_list = Meal_Type.objects.order_by('-meal_type_name')[:5]
#     context = {'latest_meal_type_list': latest_meal_type_list}
 
#     return render(request, 'home/index.html')
    objUserLogList = UserLogList()
    objUserLogList.request = request
    userlog_list = objUserLogList.get_queryset()
    context = {'userlog_list': userlog_list}
    return render(request, 'home/index.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'home/logged_out.html')

def about(request):
    return render(request, 'home/about.html')

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            # redirect, or however you want to get to the main view
            return render(request, 'home/index.html')
    else:
        form = UserForm() 

    return render(request, 'home/registration_form.html', {'form': form})

#ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#     
    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == "current":
            return self.request.user
        return super(UserViewSet, self).get_object()



# Logger with rating, Meal with Meal Type
def detail(request, meal_type_id):
    meal_type = get_object_or_404(Meal_Type, pk=meal_type_id)
    context = {'meal_type': meal_type}
    return render(request, 'home/detail.html', context)
 
def results(request, meal_type_id):
    meal_type = get_object_or_404(Meal_Type, pk=meal_type_id)
    context = {'meal_type': meal_type}
    return render(request, 'home/results.html', context)

def increase_calorie_for_meal(request, meal_type_id):
    meal_type = get_object_or_404(Meal_Type, pk=meal_type_id)
    try:
        selected_meal = meal_type.meal_set.get(pk=request.POST['meal'])
    except (KeyError, Meal.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'home/detail.html', {
            'meal_type': meal_type,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_meal.calories += 1
        selected_meal.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('home:results', args=(meal_type.id,)))

def rate(request, logger_id):
    return HttpResponse("You're rating on Logger %s." % logger_id)

