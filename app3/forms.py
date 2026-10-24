from django import forms
class Teacher(forms.Form):
    tno=forms.IntegerField()
    tname=forms.CharField()
    tdegree=forms.CharField()
   