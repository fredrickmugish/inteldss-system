from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  
        if commit:
            user.save()
        return user


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']