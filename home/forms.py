from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker

from .models import Meal_Type, Meal

class UserForm(ModelForm):  
    # last_edit_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    username = forms.CharField(max_length=100, widget=forms.TextInput)
    email = forms.CharField(max_length=100, widget=forms.TextInput)
    password = forms.CharField(max_length=100, widget=forms.TextInput)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput)
    # entry = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        # fields = "__all__"
#}   
     

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
