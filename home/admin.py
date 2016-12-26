from django.contrib import admin

from django import forms

# Register your models here.
from .models import Logger, Meal, Meal_Type

#set admin title
admin.site.site_header = 'Dyraid'
admin.site.index_title = 'Dyraid'
admin.site.site_title = 'Dyraid'


# class LoggerForm(ModelForm):
#     class Meta:
#         model = Logger
#         fields = ['last_edit_date', 'entry']
     
# Changing the html elements using forms   
class LoggerForm(forms.ModelForm):  #{
    last_edit_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    title = forms.CharField(widget=forms.TextInput)
    entry = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Logger
        # fields = ['last_edit_date', 'title', 'entry', 'rating']
        fields = "__all__"
#}   
    
class LoggerAdmin(admin.ModelAdmin):
    #form = LoggerForm
    fieldsets = [
        (None, {'fields': ['last_edit_date']}),
        ('Details', {'fields': ['title', 'entry']}),
    ]

admin.site.register(Logger, LoggerAdmin)
admin.site.register(Meal)
admin.site.register(Meal_Type)

