from django.shortcuts import render
from . import forms
# Create your views here.

def employeeinput(request):
    form=forms.Employee
    my_dict={'form':form}
    return render(request, 'app1/employee.html', context=my_dict)