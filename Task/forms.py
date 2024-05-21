from .models import Task
from django import forms
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','customer','date_from','date_to','state']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            'description':forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            'customer':forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            
            'date_from': forms.DateInput(attrs={
                'type': 'date',
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'
                }) ,
            'date_to': forms.DateInput(attrs={
                'type': 'date',
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'
                }) ,
            'state': forms.Select(attrs={'class': 'form-control'}),
        }

class RegisterForm(forms.ModelForm):
    # username = forms.CharField(label='Nombre de usuario', max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets={
            'username':forms.TextInput(attrs={'class': 'text-white shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            'email':forms.EmailInput(attrs={'class': 'text-white shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            'password':forms.PasswordInput(attrs={'class': 'text-white shadow appearance-none border rounded w-full py-2 px-3 text-white bg-gray-800 leading-tight focus:outline-none focus:shadow-outline'}),
            
        }