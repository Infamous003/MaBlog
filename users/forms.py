from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batman'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'batman@gotham.com'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Cant apply styles to password fields, need to do it manually
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**********'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**********'})


        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].help_text = None