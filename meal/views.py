from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from braces import views # Ajax Mixin included

from .models import Meal
from .forms import MealForm

# Create your views here.


class MealList(LoginRequiredMixin, generic.ListView):
    model = Meal
    # template_name = 'home/meal_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'meal_list'
    paginate_by = 2
    # queryset = Meal.objects.all()  # Default: Model.objects.all()    
    def get_queryset(self):
        # """Return the last five meal types."""
        return Meal.objects.order_by('food_name')
     
class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    
class MealDetail(LoginRequiredMixin, DetailView):
    model = Meal
    form_class = MealForm
    template_name_suffix = '_detail'
     
class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealForm
    template_name_suffix = '_update_form'
     
class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('meal:meal_list')