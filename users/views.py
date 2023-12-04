from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


def info(request):
    context = {"title": "Информация"}
    return render(request=request, template_name="users/info.html", context=context)


class MainPage(View):
    def get(self, request):
        context = {"title": "Messenger",
                   }
        #вывод всех групп пользователя
        return render(request=request, template_name="users/main_page.html", context=context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    context = {"title": "Authorize"}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    context = {"title": "Registration"}
    success_url = reverse_lazy("login")


class UserMainPage(LoginRequiredMixin, View):
    def get(self, request):
        context = {"title": "Messenger",
                   }
        return render(request=request, template_name="users/user_main_page.html", context=context)



