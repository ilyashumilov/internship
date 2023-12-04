from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required"}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required"}))
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required"}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={"placeholder": "Repeat the password", "required": "required"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        labels = {"email": "E-mail",
                  "first_name": "First name",
                  "last_name": "Last name"
                  }
        widgets = {"email": forms.TextInput(attrs={"placeholder": "E-mail", "required": "required"}),
                   }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("The email has already been registered!")
        return email
