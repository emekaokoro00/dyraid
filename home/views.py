from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Meal_Type, Meal

#after Generic View
class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'latest_meal_type_list'

    def get_queryset(self):
        """Return the last five meal types."""
        return Meal_Type.objects.order_by('meal_type_name')[:2]


class DetailView(generic.DetailView):
    model = Meal_Type
    template_name = 'home/detail.html'


class ResultsView(generic.DetailView):
    model = Meal_Type
    template_name = 'home/results.html'


# def index(request):
#     latest_meal_type_list = Meal_Type.objects.order_by('-meal_type_name')[:5]
#     context = {'latest_meal_type_list': latest_meal_type_list}
#     return render(request, 'home/index.html', context)
# 
# # Logger with rating, Meal with Meal Type
# def detail(request, meal_type_id):
#     meal_type = get_object_or_404(Meal_Type, pk=meal_type_id)
#     context = {'meal_type': meal_type}
#     return render(request, 'home/detail.html', context)
# 
# def results(request, meal_type_id):
#     meal_type = get_object_or_404(Meal_Type, pk=meal_type_id)
#     context = {'meal_type': meal_type}
#     return render(request, 'home/results.html', context)

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