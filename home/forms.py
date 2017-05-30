from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker

from .models import UserProfile, User_Type, Sex

# class UserForm(ModelForm):  
class UserProfileForm(ModelForm):  
    # last_edit_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    username = forms.CharField(max_length=100, widget=forms.TextInput)
    email = forms.CharField(max_length=100, widget=forms.TextInput)
    # password = forms.CharField(max_length=100, widget=forms.TextInput)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput)
    # date_of_birth = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
    user_type = forms.ChoiceField(choices=[(e.value, e.name.replace("_", " ")) for e in User_Type])
    sex_type = forms.ChoiceField(choices=[(e.value, e.name.replace("_", " ")) for e in Sex])
    # user_type_choices = [(e.name, e.value) for e in User_Type]
    # user_type = forms.ChoiceField(choices=user_type_choices)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'user_type', 'sex_type')
        # fields = "__all__"
        
    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Save your profile
        profile = UserProfile()
        profile.user = user
        # profile.date_of_birth = self.cleaned_data['date_of_birth']
        profile.user_type = self.cleaned_data['user_type']
        profile.sex_type = self.cleaned_data['sex_type']
        profile.check_comment = 'start'
        profile.save()
#}  
 
        
