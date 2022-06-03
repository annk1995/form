
# from datetime import datetime
# from django import forms
# from .models import Users
# from django.utils import timezone

# class User(forms.Form):
#    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'})) 
   
#    email= forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))
#    date_created= forms.DateField(label="Date") 
#    time_stamp= forms.DateTimeField(label="Time")
#    role= forms.ChoiceField(label="Role", choices=[('admin','Admin'),('manager','Manager'),('supervisor','Supervisor'),('employee','Employee')])
#    spirit_animal=forms.CharField(label="Spirit Animal")
# class Users(forms.Modelforms):
#     class Meta:
#         model =Users
#         fields =('name')
from pyexpat import model
from django import forms
from psutil import users
from .models import  Users
from django.contrib.auth.models import User

class User(forms.Form):
    DEMO_CHOICES =(
    ("Mgr", "Manager"),
    ("Emp", "Employee"),
    ("Admin", "Administrator"),
    ("Sup", "Supervisor"),
    )
    username = forms.CharField()
    spirit_animal = forms.CharField()
    roles = forms.ChoiceField(choices = DEMO_CHOICES)
    
    
    class Meta: 
        model = Users
        fields = ['username', 'spirit_animal', 'roles']  
    
    
    
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email','spirit_animal','roles')
        labels = {
            'name': 'Username',
            'email': 'Email',
            'spirit_animal': 'Spirit Animal',
            'roles': 'Roles',
            
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Username', 'style': 'max-width: 700px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your email', 'style': 'max-width: 700px;'}),
            'spirit_animal': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Spirt Animal', 'style': 'max-width: 700px;'}),
            'roles': forms.Select(attrs={'class': 'form-control', 'placeholder':'Your role', 'style': 'max-width: 700px;'}),
            
        }  
              