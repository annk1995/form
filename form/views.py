import email
from django.shortcuts import render
from django import forms
from form.models import Users
from .forms import SnippetForm, Users
from django.http import HttpResponse

from form import forms



# Create your views here.
def get_name(request):
    if request.method =='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            name =form.cleaned_data['name']
            email=form.cleaned_data['email']
            return render(request,'form.html',{'form':form})
        return render(request,'form.html',{'form':form})
        
            

    form=SnippetForm()
    return render(request,'form.html',{'form':form})
    

# def user_detail(request):
#     if request.method =='POST':
#      form=User(request.POST)
#     if form.is_valid():
#             name =form.cleaned_data['name']
#             email=form.cleaned_data['email']
            

#     form=Users()
#     return render(request,'form.html',{'form':form})

             