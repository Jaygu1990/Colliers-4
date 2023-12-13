from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="main"),
    path("logout",views.user_logout,name="logout"),
    path("login",views.user_login,name="login")
]