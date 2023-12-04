from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("info/", views.info, name="info"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("account/logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("account/", views.UserMainPage.as_view(), name="account"),
]