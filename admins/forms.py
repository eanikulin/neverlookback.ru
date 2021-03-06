from django import forms
from users.models import User
from users.forms import UserRegistrationForm, UserProfileForm


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = (
        'username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2', 'middle_name', 'age')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
