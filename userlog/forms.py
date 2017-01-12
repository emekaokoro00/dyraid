from django import forms

from bootstrap3_datetime.widgets import DateTimePicker

from .models import  UserLog


  
class UserLogForm(forms.ModelForm):  #{        
    def __init__(self, *args, **kwargs):
        super(UserLogForm, self).__init__(*args, **kwargs)        
        self.fields['meal'].required = True 
        self.fields['log_time'].required = True 
        self.fields['log_time'].widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"})         
        self.fields['comment'].required = False  
        self.fields['comment'].widget=forms.Textarea(attrs={'required':False})       
    class Meta:
        model = UserLog
        fields = ['meal', 'log_time', 'comment']
#}  