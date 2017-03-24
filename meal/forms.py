from django import forms

from bootstrap3_datetime.widgets import DateTimePicker

from .models import  Meal
 
class MealForm(forms.ModelForm):    
    food_name = forms.CharField(max_length=100, widget=forms.TextInput, required=True)
    # food_type = forms.ChoiceField(widget=forms.Select)
    calories = forms.IntegerField(widget=forms.NumberInput)
    def send_calorie_number(self):
        # send calorie number
        pass
    class Meta:
        model = Meal
        fields = ['food_name', 'food_type', 'calories', 'restaurant_offering']  
#}  