
from django.shortcuts import render
from django.http import HttpResponse
from .models import School
from . import forms

def school(request):
    school_data = School.objects.all()

    my_dict = {
        'school_list': school_data
    }

    return render(request, 'app1/school.html', context=my_dict)

def studentinputview(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'app1/input.html', context=my_dict)