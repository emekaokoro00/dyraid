from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .forms import UserForm
from django.contrib.auth.models import User

# Create your views here.
from .models import Meal_Type, Meal


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