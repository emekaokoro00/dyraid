from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.forms.models import ModelForm

from django.contrib.auth.models import User

# Create your views here.
from .models import Meal_Type, Meal
from .forms import UserForm, MealForm


#NOTES
#Currently you use the admin login
#You can create your own login ... check "https://docs.djangoproject.com/en/1.10/topics/auth/default/"
@login_required() # settings for redirect found in settings.py - LOGIN_URL
def index(request):
    latest_meal_type_list = Meal_Type.objects.order_by('-meal_type_name')[:5]
    context = {'latest_meal_type_list': latest_meal_type_list}
    return render(request, 'home/index.html')

def logout_view(request):
    logout(request)
    return render(request, 'home/logged_out.html')

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
 
class MealList(generic.ListView):
    model = Meal
    context_object_name = 'meal_list' 
    def get_queryset(self):
        # """Return the last five meal types."""
        return Meal.objects.order_by('food_name')[:10]
     
class MealCreate(CreateView):
    model = Meal
    fields = ['food_name', 'food_type', 'calories']
    
class MealDetail(DetailView):
    model = Meal
    fields = ['food_name', 'food_type', 'calories']
    template_name_suffix = '_detail'
     
class MealUpdate(UpdateView):
    model = Meal
    fields = ['food_name', 'food_type', 'calories']
    template_name_suffix = '_update_form'
     
class MealDelete(DeleteView):
    model = Meal
    success_url = reverse_lazy('home:meal_list')

# #after Generic View
# class IndexView(generic.ListView):
#     template_name = 'home/index.html'
#     context_object_name = 'latest_meal_type_list'
# 
#     def get_queryset(self):
#         """Return the last five meal types."""
#         return Meal_Type.objects.order_by('meal_type_name')[:4]
# 
# 
# class DetailView(generic.DetailView):
#     model = Meal_Type
#     template_name = 'home/detail.html'
# 
# 
# class ResultsView(generic.DetailView):
#     model = Meal_Type
#     template_name = 'home/results.html'