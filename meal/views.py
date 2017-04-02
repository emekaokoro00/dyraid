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
    

#FBV
# def meal_list(request, template_name='home/meal_list.html'):
#     meal_list = Meal.objects.all()
# #     data = {}
# #     data['object_list'] = meals
# #     return render(request, template_name, data)
#     context = {'meal_list':meal_list}
#     return render(request, template_name, context)
#     
# def meal_create(request, template_name='home/meal_form.html'):
#     form = MealForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('meal_list')
#     return render(request, template_name, {'form':form})  
# 
# def meal_detail(request, pk, template_name='home/meal_detail.html'):
#     meal = get_object_or_404(Meal, pk=pk)
#     form = MealDetailForm(request.POST or None, instance=meal)
#     context = {'meal':meal}
#     return render(request, template_name, context)
#     
# def meal_update(request, pk, template_name='home/meal_form.html'):
#     meal = get_object_or_404(Meal, pk=pk)
#     form = MealForm(request.POST or None, instance=meal)
#     if form.is_valid():
#         form.save()
#         return redirect('home:meal_list')
#     return render(request, template_name, {'form':form})
#     
# def meal_delete(request, pk, template_name='home/meal_confirm_delete.html'):
#     meal = get_object_or_404(Meal, pk=pk)
#     form = MealForm(request.POST or None, instance=meal)
#     if request.method=='POST':
#         meal.delete()
#         return redirect('meal_list')
#     return render(request, template_name, {'object':meal})


#CBV
# class MealSendCaloriesView(FormView):
#     template_name = 'home/generic_action.html'
#     form_class = MealSendCaloriesForm
#     success_url = 'home/thanks/'
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed
#         # It should retunr an HttpResponse
#         form.send_calorie_number()
#         return super(MealSendCaloriesView, self).form_valid(form)

#LoginRequiredMixin to make sure that user is logged in, redirects to url in settings