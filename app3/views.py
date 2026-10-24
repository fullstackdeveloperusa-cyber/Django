from django.shortcuts import render
from . import forms
# Create your views here.

def Teacherinput(request):
    form=forms.Teacher
    my_dict={'form':form}
    return render(request, 'app1/teacher.html', context=my_dict)