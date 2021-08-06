 
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.list import ListView
from . models import * 
from .models import *
from django import forms
# Create your views here.

class AddDetail(CreateView):
    model = Student
    fields = ['name','email','desc','img']
    template_name= 'detail.html'
    success_url = 'detail'

    def get_form(self) :
        form= super().get_form() 
        form.fields['name'].widget  = forms.TextInput(attrs={'class':'form-control'}) 
        form.fields['email'].widget  = forms.EmailInput(attrs={'class':'form-control'})
        form.fields['desc'].widget  = forms.Textarea(attrs={'class':'form-control'})
        # form.fields['img'] = Student(self.request.POST, self.request.FILES)
            
         
        return form 

class UpdateStudent(UpdateView):
    model = Student
    fields = ['name','email','desc','img']
    template_name= 'detail.html'
    success_url = 'http://127.0.0.1:8000/detail/'



class DeleteStudent(DeleteView):
    model = Student
    template_name = 'delete.html'
    success_url = 'http://127.0.0.1:8000/detail/'


class DetailListView(ListView):
    model = Student
    template_name = 'index.html'