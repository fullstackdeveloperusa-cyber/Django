from django import forms
class Employee(forms.Form):
    eno=forms.IntegerField()
    ename=forms.CharField()
    esal=forms.IntegerField()
    eaddr=forms.CharField()