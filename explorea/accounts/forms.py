from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from core.validators import validate_human_name

from .models import Profile

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    # cutom made validator
    first_name = forms.CharField(max_length=100, validators=[validate_human_name,])
    last_name = forms.CharField(max_length=100, validators=[validate_human_name,])
    
    class Meta:
        model = UserModel 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

class EditUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, validators=[validate_human_name,])
    last_name = forms.CharField(max_length=100, validators=[validate_human_name,])
    
    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'avatar',]