from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    # attrsのform-controlを反映させるために、直接指定する
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1 mb-3'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-1 mb-3'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-1 mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1 mb-3'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
