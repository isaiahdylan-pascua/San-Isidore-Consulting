from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee

class user_form(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['EmployeeName ', 'password1', 'password2', "Occupation", 
                  "DateofEmployment", "EmployeeStreet", "EmployeeBarangay", "EmployeeCity",
                  "EmployeeProvince", "EmployeeZipCode"]
