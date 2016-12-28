from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):       
        
    # last_edit_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    username = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.TextInput)
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    # entry = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
#}   