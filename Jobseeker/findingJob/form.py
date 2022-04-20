from django.forms import ModelForm, TextInput, Select, DateInput, Textarea, ChoiceField
from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'groups']


class JobdetailForm(ModelForm):
    class Meta:
        model = jobdetail
        # fields = ['title', 'location', 'type']
        fields = ['title', 'location', 'type', 'salary', 'company_details', 'published_date', 'deadline_date',
                  'no_of_vaccinies', 'description', 'responsibility', 'qualification', 'company_logo', 'jobcategory']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title',
                'id': "form6Example1",
            }),

            'salary': TextInput(attrs={
                'type': 'Float',
                'class': "form-control",
                'placeholder': 'Salary',
                'id': "form6Example2",
            }),

            'company_details': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Company Description',
                'id': "form6Example2",
            }),

            'location': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'location',
                'id': "form6Example4",
            }),

            'type': Select(attrs={
                'class': "form-control",
                'placeholder': 'location',
                'id': "form6Example4",
            }),

            'published_date': DateInput(attrs={
                'type': 'date',
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'mm/dd/yyyy',
                'required': True,
            }),
            'deadline_date': DateInput(attrs={
                'type': 'date',
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'mm/dd/yyyy',
                'required': True,
            }),

            'no_of_vaccinies': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'No of vacancy',
                'id': "form6Example1",
            }),

            'description': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Job Description',
                'id': "form6Example2",
            }),

            'responsibility': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Job Responsibility',
                'id': "form6Example2",
            }),

            'qualification': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Qualification',
                'id': "form6Example2",
            }),

        }

